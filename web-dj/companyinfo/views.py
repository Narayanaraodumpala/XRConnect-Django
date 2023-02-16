from cgitb import reset
from django.shortcuts import render
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Companyinfo
from django.http import HttpResponse
from .serializers import CompanyinfoSerializers,GetCompanyDetailsSerializers,GetCompanyBasedListSerializers,DeleteCompanySerializers,UpdateCompanySerializers
from rest_framework import status, generics, views
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import time
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
sender_address = 'support@xrconnect.io'
sender_pass = 'support@!23'
socket.getaddrinfo('localhost', 8080)
if __name__ == '__main__':
    pass
import io

# Create your views here.
class  AddCompany(generics.GenericAPIView):
       serializer_class=CompanyinfoSerializers
    #    token_param_config = openapi.Parameter(
    #     'company_id', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)

       
       permission_classes=(IsAuthenticated,)
       #@swagger_auto_schema(manual_parameters=[token_param_config])
       def post(self, request):
           if  request.method == "POST":
            try:
                startime=time.time()
                res = request.data
                serializer =CompanyinfoSerializers(data=res)
                print(res)
                if serializer.is_valid():
                    serializer.save()
                    endtime=time.time()
                    return Response(
                        {'message': 'company data saved successfully', 'status': 'success', 'Time taken':endtime - startime, 'code': status.HTTP_201_CREATED, })
                else:
                    return Response({'error': serializer.errors, 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST})



            except KeyError:
                return Response({'message': 'error',
                                'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)
                
            
class GetCompanyDetails (generics.GenericAPIView):
    #permission_classes=(IsAuthenticated,)
    # token_param_config = openapi.Parameter(
    # 'company_id', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)
    # @swagger_auto_schema(manual_parameters=[token_param_config])
    serializer_class=GetCompanyDetailsSerializers
    
    def post(self, request):
        if  request.method == "POST":
            try:
                startime=time.time()
                company_id = request.data['company_id']
                print('company is=',company_id)
                
                data = Companyinfo.objects.filter(company_id=company_id)
                if data:
                    serializers = CompanyinfoSerializers(data, many=True)
                    endtime=time.time()
                    return Response({'status': 'success', 'code': status.HTTP_200_OK, 'Time taken':endtime - startime, 'company details': serializers.data},
                                    status=status.HTTP_200_OK)
                else:
                    error = {'error': 'invalid company_id '}
                return Response({'message': error, 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)
            except KeyError:
                return Response({'status': 'failed', 'message': ' missing company_id ',
                                'code': status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)


class GetCompanyList(APIView):
    #permission_classes=(IsAuthenticated,)
    def get(self, request):
        starttime=time.time()
        queryset = Companyinfo.objects.all()
        serializers = CompanyinfoSerializers(queryset, many=True)
        endtime=time.time()
        return Response({'status': 'success', 'code': status.HTTP_200_OK, 'Time taken':endtime - starttime,'company info': serializers.data},
                        status=status.HTTP_200_OK)

class GetCompanyBasedList (generics.GenericAPIView):
    serializer_class=GetCompanyBasedListSerializers
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        if  request.method == "POST":
            try:
                starttime=time.time()
                company_name = request.data['company_name']
                
                data = Companyinfo.objects.filter(company_name=company_name)
                if data:
                    serializers = CompanyinfoSerializers(data, many=True)
                    endtime=time.time()
                    return Response({'status': 'success', 'code': status.HTTP_200_OK, 'Time taken':endtime - starttime,'company details': serializers.data},
                                    status=status.HTTP_200_OK)
                else:
                    error = {'error': 'invalid company_name '}
                return Response({'message': error, 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)
            except KeyError:
                return Response({'status': 'failed', 'message': ' missing company_id ',
                                'code': status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)         
            


class DeleteCompany(generics.GenericAPIView):
    serializer_class=DeleteCompanySerializers
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        if  request.method == "POST":
            try:
                starttime=time.time()
                company_id = request.data['company_id']
                user = Companyinfo.objects.filter(company_id=company_id).delete()
                if user[0] != 0:
                    endtime=time.time()
                    return Response(
                        {'status': 'success', 'message': 'company successfully', 'Time taken':endtime - starttime,'code': status.HTTP_200_OK},
                        status=status.HTTP_200_OK)

                else:
                    return Response({'message': 'invalid comapany id', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                                    status=status.HTTP_400_BAD_REQUEST)
            except KeyError:
                return Response(
                    {'message': 'company_id required', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                    status=status.HTTP_400_BAD_REQUEST)
    from rest_framework.renderers import JSONRenderer

class UpdateCompany(generics.GenericAPIView):
    serializer_class=UpdateCompanySerializers
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        if  request.method == "POST":
            starttime=time.time()
            global json_data
            b_data = request.body
            streamed = io.BytesIO(b_data)
            d1 = JSONParser().parse(streamed)
            user = d1.get('company_id', None)
            if user:
                try:
                    res = Companyinfo.objects.get(company_id=user)
                    serializers = CompanyinfoSerializers(res, d1, partial=True)
                    if serializers.is_valid():
                        serializers.save()
                        endtime=time.time()
                        message = {'status': 'success', 'message': 'comapany updated successfully','Time taken':endtime - starttime,
                                'code': status.HTTP_201_CREATED}
                        json_data = JSONRenderer().render(message
                                                        )
                        return HttpResponse(json_data, content_type='application/json', status=status.HTTP_201_CREATED)
                    # else: message = {'status': 'failed', 'message': serializers.errors, 'code':
                    # status.HTTP_400_BAD_REQUEST} json_data = JSONRenderer().render(message) return HttpResponse(
                    # json_data, content_type='application/json', status=status.HTTP_400_BAD_REQUEST)
                except CompanyinfoSerializers.DoesNotExist:
                    message = {'status': 'failed', 'message': 'invalid comapny_id',
                            'code': status.HTTP_400_BAD_REQUEST}
                    json_data = JSONRenderer().render(message)
                    return HttpResponse(json_data, content_type='application/json', status=status.HTTP_201_CREATED)

            else:
                message = {'status': 'failed', 'message': 'please provide comapnyid',
                        'code': status.HTTP_400_BAD_REQUEST}
                json_data = JSONRenderer().render(message)
            return HttpResponse(json_data, content_type='application/json', status=status.HTTP_201_CREATED)