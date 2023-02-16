# import all packages and references which are needed for business logic development  in login views
import io
from sys import api_version
from rest_framework import pagination
from datetime import timedelta
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from django.shortcuts import render, get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import jwt
import time
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status, generics, views
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.urls import reverse
from .serializers import RegistrationSerializer, EmailVerificationSerializer, \
    ResetPasswordEmailRequestSerializer, \
    SetNewPasswordSerializer, LoginSerializer,AddUserSerializers,GetCompanyuserListSerializers\
        ,VrLoginSerializers,GetCompanyUsersListSerializers,Generatevrcodeserializers,GetAllUsersSerializers,UpdateUserSerializer,DeleteUserSerializers,GetOneUserUserSerializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import PageNumberPagination
from django.utils.encoding import smart_str, smart_bytes, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .models import RegisterModel
import random
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .paginartion import CustomPagination
from django.db import IntegrityError
import socket
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
import threading

from login import serializers

from login import paginartion

# @swagger_auto_schema{
    
# }

# declaring sender email address and password for sending token once users resister successfully..

sender_address = 'support@xrconnect.io'
sender_pass = 'support@!23'
socket.getaddrinfo('localhost', 8080)
if __name__ == '__main__':
    pass


def index(request):
    return HttpResponse("Hello, world. You're at the login index.")


# class EmailThread(threading.Thread):
#     def __init__(self, reciver_mail):
#         self.reciver_mail = reciver_mail
#         threading.Thread.__init__(self)
#
#     def run(self):
#         self.reciver_mail.send(fail_silently=True)


''' resister the users into login/register model and generate 
jwt token and send it to users email address, 
if having any errors through error message to users '''


class RegisterView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    permission_classes=()

    def post(self, request):
        startime=time.time()
        try:
            data = request.data
            serializer = RegistrationSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                user_data = serializer.data
                user = RegisterModel.objects.get(email=user_data['email'])
                token = RefreshToken.for_user(user).access_token
                token.set_exp(lifetime=timedelta(days=36500))
                current_site = get_current_site(request).domain
                relativeLink = reverse('email-verify')
                absurl = 'http://' + current_site + relativeLink + "?token=" + str(token)
                reciver_mail = user.email
                message = MIMEMultipart()
                message['From'] = sender_address
                message['To'] = reciver_mail
                message['Subject'] = 'Registration confirmation! '
                mail_content = 'hello' + ' ' + user.user_name + ' please click this below  link to verify your account ' \
                                                                '\n ' + absurl
                message.attach(MIMEText(mail_content, 'plain'))
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender_address, sender_pass)
                text = message.as_string()
                s.sendmail(sender_address, reciver_mail, text)
                s.quit()
                endtime=time.time()
                return Response({
                    'data': '', 'message': 'signup successful,please verify your account',
                    'code': status.HTTP_201_CREATED,'Time taken':endtime - startime,
                }, status=status.HTTP_201_CREATED)
            else:
                data = serializer.errors
            return Response({
                'status': 'failed', 'message': serializer.errors, 'code': status.HTTP_400_BAD_REQUEST},
                status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError as e:
            account = RegisterModel.objects.get(user_name='')
            account.delete()
            raise ValidationError({"400": f'{str(e)}'})
        except KeyError as e:
            print(e)
            raise ValidationError({"400": f'Field {str(e)} missing'})
        except TypeError:
            return Response({
                'status': 'failed', 'message': ' user_name field is required ', 'code': status.HTTP_400_BAD_REQUEST},
                status=status.HTTP_400_BAD_REQUEST)


# verifying the users token weather exact token or not , if not through error message...

class VerifyEmail(views.APIView):
    permission_classes=()
    serializer_class = EmailVerificationSerializer
    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        startime=time.time()
        token = request.GET.get('token')
        print('token=', token)
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            print('-----------')
            print(payload)

            user = RegisterModel.objects.get(id=payload['user_id'])
            if not user.is_active:
                user.is_active = True
                user.save()
                endtime=time.time()

            return Response({'message': 'email verified successfully','status':'success', 'code': status.HTTP_200_OK,'Time taken':endtime - startime,},
                            status=status.HTTP_200_OK,)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'message': 'Activation Expired','status':'failed', 'code': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'message': 'invalid token','status':'failed', 'code': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)


'''accessing users login , generating access_token and refresh_token 
if credentials was correct , else through error message '''


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes=()

    def post(self, request):
        startime=time.time()
        try:
            res_serializer = LoginSerializer(data=request.data)
            if res_serializer.is_valid():
                serializer = self.serializer_class(data=request.data)
                serializer.is_valid(raise_exception=True)
                user = request.data['email']
                user_data = RegisterModel.objects.get(email=user)
                
                if user_data.is_active:
                    endtime=time.time()
                    return Response(
                        {'message': 'login success', 'status': 'success', 'details': serializer.data,
                         'user_name': user_data.user_name, 'gender': user_data.gender,
                         'role': user_data.role,'company':user_data.company_name,'Time taken':endtime - startime},
                        status=status.HTTP_200_OK)
                else:
                    return Response(
                        {'message': 'Account not verified',
                         'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST})


            else:
                return Response({
                    'status': 'failed', 'message': res_serializer.errors, 'code': status.HTTP_400_BAD_REQUEST},
                    status=status.HTTP_400_BAD_REQUEST)

        except RegisterModel.DoesNotExist:
            return Response({'message': 'invalid email', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer
    permission_classes=()

    def post(self, request):
        startime=time.time()
        data = {'request': request, 'data': request.data}
        serializer = self.serializer_class(data=request.data)
        email = request.data['email']
        if RegisterModel.objects.filter(email=email).exists():
            user = RegisterModel.objects.get(email=email)
            reciver_mail = user.email
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request=request).domain
            relativeLink = reverse('password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
            absurl = 'http://' + current_site + relativeLink
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = reciver_mail
            message['Subject'] = 'Reset your Password! '
            mail_content = 'hello \n  please use this link to reset your password \n ' + absurl
            message.attach(MIMEText(mail_content, 'plain'))
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(sender_address, sender_pass)
            text = message.as_string()
            s.sendmail(sender_address, reciver_mail, text)
            s.quit()
            endtime=time.time()

        return Response({'status': 'success', 'message': 'we have sent you a link to rest your password','Time taken':endtime - startime,
                         'code': status.HTTP_200_OK},
                        status=status.HTTP_200_OK)


class PasswordTokenCheckAPi(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer
    permission_classes=()

    def get(self, request, uidb64, token):
        startime=time.time()
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = RegisterModel.objects.get(id=id)
            endtime=time.time()
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'status': 'failed', 'message': 'invalid token', 'code': status.HTTP_401_UNAUTHORIZED},
                                status=status.HTTP_401_UNAUTHORIZED)

            return Response(
                {'status': 'success', 'message': 'credentials valid','Time taken':endtime - startime, 'code': 'status.HTTP_200_OK', 'uidb64': uidb64,
                 'token': token},
                status=status.HTTP_200_OK)

        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response({'status': 'failed', 'message': 'invalid token',
                                 'code': status.HTTP_401_UNAUTHORIZED},
                                status=status.HTTP_401_UNAUTHORIZED)


class SetNewpASSWORDApiview(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer
    permission_classes=()

    def patch(self, request):
        startime=time.time()
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        endtime=time.time()
        return Response({'status': 'success', 'message': 'Password reset success', 'Time taken':endtime - startime,'code': status.HTTP_200_OK},
                        status=status.HTTP_200_OK)


''' list all the users which are present in register model   '''


class GetAllUsers(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class=GetAllUsersSerializers
    def get(self, request):
        startime=time.time()
       
        queryset = RegisterModel.objects.all()
        serializers = RegistrationSerializer(queryset, many=True)
        endtime=time.time()
       
        return Response({'status': 'success', 'code': status.HTTP_200_OK,'Time taken':endtime - startime, 'usersList': serializers.data},
                        status=status.HTTP_200_OK)


''' list one users data  based on users email from registered-model   '''


class GetOneUser(generics.GenericAPIView):
    serializer_class = GetOneUserUserSerializers
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        if  request.method == "POST":
            startime=time.time()
            try:
                email = request.data['email']
                querset = RegisterModel.objects.get(email=email)
                if querset:
                    serializers = RegistrationSerializer(querset)
                    endtime=time.time()
                    return Response({'status': 'success', 'code': status.HTTP_200_OK, 'Time taken':endtime - startime,'data': serializers.data},
                                    status=status.HTTP_200_OK)

            except RegisterModel.DoesNotExist:

                return Response({'message': 'invalid email', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)
            except KeyError:
                return Response({'message': 'email field is required', 'status': 'failed',
                                'code': status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)


''' delete  one users data  based on users email from registered-model   '''


class DeleteUser(generics.GenericAPIView):
    serializer_class = DeleteUserSerializers
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        if  request.method == "POST":
            startime=time.time()
            try:
                email = request.data['email']
                user = RegisterModel.objects.filter(email=email).delete()
                if user[0] != 0:
                    endtime=time.time()
                    return Response(
                        {'status': 'success', 'message': 'user deleted successfully','Time taken':endtime - startime, 'code': status.HTTP_200_OK},
                        status=status.HTTP_200_OK)
                    

                else:
                    return Response({'message': 'invalid email', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                                    status=status.HTTP_400_BAD_REQUEST)
            except KeyError:
                return Response(
                    {'message': 'email field required', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                    status=status.HTTP_400_BAD_REQUEST)


''' update one users data  based on users email from registermodel   '''


class UpdateUser(generics.GenericAPIView):
    serializer_class = UpdateUserSerializer

    permission_classes=(IsAuthenticated,)
    def post(self, request):
        if  request.method == "POST":
            startime=time.time()
            global json_data
            b_data = request.body
            streamed = io.BytesIO(b_data)
            d1 = JSONParser().parse(streamed)
            user = d1.get('email', None)
            if user:
                try:
                    res = RegisterModel.objects.get(email=user)
                    serializers = RegistrationSerializer(res, d1, partial=True)
                    if serializers.is_valid():
                        serializers.save()
                        endtime=time.time()
                        message = {'status': 'success', 'message': 'user updated successfully','Time taken':endtime - startime,
                                'code': status.HTTP_201_CREATED}
                        json_data = JSONRenderer().render(message
                                                        )
                        return HttpResponse(json_data, content_type='application/json', status=status.HTTP_201_CREATED)
                    # else: message = {'status': 'failed', 'message': serializers.errors, 'code':
                    # status.HTTP_400_BAD_REQUEST} json_data = JSONRenderer().render(message) return HttpResponse(
                    # json_data, content_type='application/json', status=status.HTTP_400_BAD_REQUEST)
                except RegisterModel.DoesNotExist:
                    message = {'status': 'failed', 'message': 'invalid email',
                            'code': status.HTTP_400_BAD_REQUEST}
                    json_data = JSONRenderer().render(message)
                    return HttpResponse(json_data, content_type='application/json', status=status.HTTP_201_CREATED)

            else:
                message = {'status': 'failed', 'message': 'please provide email',
                        'code': status.HTTP_400_BAD_REQUEST}
                json_data = JSONRenderer().render(message)
            return HttpResponse(json_data, content_type='application/json', status=status.HTTP_201_CREATED)
    
class AddUser(generics.GenericAPIView):
    serializer_class = AddUserSerializers
    permission_classes = (IsAuthenticated,)
    def post(self, request):
            startime=time.time()
            try:
                data = request.data
                serializer = AddUserSerializers(data=data)
                password='password@123'
                
               
                if serializer.is_valid():
                    print('-----')
                    RegisterModel.objects.create(user_name=request.data['user_name'],
                                                 email=request.data['email'],
                                                 password=password, 
                                                 gender=request.data['gender'], 
                                                 first_name=request.data['first_name'], 
                                                 last_name=request.data['last_name'],
                                                 phone_number=request.data['phone_number'])
                    print('request arrived')
                    user_data = serializer.data
                   
                    user = RegisterModel.objects.get(email=user_data['email'])
                    token = RefreshToken.for_user(user).access_token
                    token.set_exp(lifetime=timedelta(days=36500))
                    current_site = get_current_site(request).domain
                    relativeLink = reverse('email-verify')
                    absurl = 'http://' + current_site + relativeLink + "?token=" + str(token)
                    reciver_mail = user.email
                    message = MIMEMultipart()
                    message['From'] = sender_address
                    message['To'] = reciver_mail
                    message['Subject'] = 'Welcome to Xrconnect! '
                    mail_content = 'hello' + ' ' + user.user_name + ' please click this below  link to verify your account ' \
                                                                    '\n ' + absurl
                    message.attach(MIMEText(mail_content, 'plain'))
                    s = smtplib.SMTP('smtp.gmail.com', 587)
                    s.starttls()
                    s.login(sender_address, sender_pass)
                    text = message.as_string()
                    s.sendmail(sender_address, reciver_mail, text)
                    s.quit()
                    endtime=time.time()
                    return Response({
                        'data': '', 'message': 'signup successful,please verify your account','Time taken':endtime - startime,
                        'code': status.HTTP_201_CREATED
                    }, status=status.HTTP_201_CREATED)
                else:
                    data = serializer.errors
                return Response({
                    'status': 'failed', 'message': serializer.errors, 'code': status.HTTP_400_BAD_REQUEST},
                    status=status.HTTP_400_BAD_REQUEST)
            except IntegrityError as e:
                account = RegisterModel.objects.get(user_name='')
                account.delete()
                raise ValidationError({"400": f'{str(e)}'})
            except KeyError as e:
                print(e)
                raise ValidationError({"400": f'Field {str(e)} missing'})
            # except TypeError:
            #     return Response({
            #         'status': 'failed', 'message': ' user_name field is required ', 'code': status.HTTP_400_BAD_REQUEST},
            #         status=status.HTTP_400_BAD_REQUEST)


class GetCompanyUsersList(generics.GenericAPIView):
    serializer_class=GetCompanyUsersListSerializers
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        startime=time.time()
        try:
            company_name = request.data['company_name']
            querset = RegisterModel.objects.filter(company_name=company_name)
            print(querset)
            if querset:
                serializers = GetCompanyuserListSerializers(querset,many=True)
                endtime=time.time()
                return Response({'status': 'success', 'code': status.HTTP_200_OK, 'data': serializers.data},
                                status=status.HTTP_200_OK)

        except RegisterModel.DoesNotExist:

            return Response({'message': 'invalid company_name', 'Time taken':endtime - startime,'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({'message': 'company_name field is required', 'status': 'failed',
                             'code': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)
    


    
    # page_size = 10
    # def get(self, request):
    #     page_size = 10
    #     queryset = RegisterModel.objects.all()
    #     paginator = PageNumberPagination()
    #     paginator.page_size = page_size
    #     result_page = paginator.paginate_queryset(queryset=queryset)
    #     serializer = RegistrationSerializer(result_page, many=True)
    #     return paginator.get_paginated_response(serializer.data)
       

    # def get(self, request):
    #     class Meta:if request.method=='POST':
            
    #         def get_queryset(self):
    #             queryset = RegisterModel.objects.all()
    #             return queryset
            

class Getuserpaginationlist(ModelViewSet):
    
    permission_classes=(IsAuthenticated,)
    queryset=RegisterModel.objects.all()
    serializer_class=RegistrationSerializer
    paginartion_class=PageNumberPagination
    

class Generatevrcode(generics.GenericAPIView):
     serializer_class=Generatevrcodeserializers
     
     permission_classes=(IsAuthenticated,)
    #  @swagger_auto_schema(
    #      manual_parameters=[
    #          openapi.Parameter('email', in_=openapi.IN_QUERY,
    #                            type=openapi.TYPE_STRING)
    #      ]) 
    
     def post(self, request):
         if  request.method == "POST":
            startime=time.time()
            try:
                email = request.data['email']
                querset = RegisterModel.objects.get(email=email)
                if querset:
                    otp=random.randint(9999,1000000)
                    querset.vrcode=otp
                    querset.save()
                    endtime=time.time()
                    return Response({'status': 'success', 'code': status.HTTP_200_OK,'Time taken':endtime - startime, 'vrcode':otp },
                                    status=status.HTTP_200_OK)

            except RegisterModel.DoesNotExist:

                return Response({'message': 'invalid email', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)
            except KeyError:
                return Response({'message': 'email field is required', 'status': 'failed',
                                'code': status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)

class Vrlogin(generics.GenericAPIView):
     serializer_class=VrLoginSerializers
     permission_classes=(IsAuthenticated,)
     def post(self,request):
         if  request.method == "POST":
             startime=time.time()
             try:
                 vrcode = request.data["vrcode"]
                 user=RegisterModel.objects.filter(vrcode=vrcode).first()
                
                 if user:
                     
                     
                     
                     userData = {
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "user_name": user.user_name,
                "vr code":user.vrcode,
                
            }    
                     user.vrcode=' '
                     user.save()
                     endtime=time.time()
                     return Response({'status': 'success', 'code': status.HTTP_200_OK,'Time taken':endtime - startime, 'data': userData},
                                status=status.HTTP_200_OK)
                 else:
                     return Response({'message': 'no existing vrcode , please generate vrcode and login again', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)
                 
                    
                     
             except RegisterModel.DoesNotExist:
                 return Response({'message': 'invalid vrcode', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)
             except KeyError:
              return Response({'message': 'vrcode field is required', 'status': 'failed',
                             'code': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)

                 
                 