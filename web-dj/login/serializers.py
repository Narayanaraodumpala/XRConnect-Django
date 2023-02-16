# creating serializers for login app and models

from rest_framework import serializers, status
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

from .models import RegisterModel
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import socket

sender_address = 'support@xrconnect.io'
sender_pass = 'support@!23'
socket.getaddrinfo('localhost', 8080)
''' creating serializer class for RegisterModel with named 
RegistrationSerializer with below criteria '''


def validate_email(email):
    email = RegisterModel.objects.filter(email=email)
    if email:
        raise serializers.ValidationError('user with this email already exists')


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    email = serializers.EmailField(validators=[validate_email])

    default_error_messages = {
        'user_name': 'The user_name should only contain alphanumeric characters'}

    class Meta:
        model = RegisterModel
        fields = (
            'id',
            'user_name',
            'email',
            'password',
            'gender',

        )

        extra_kwargs = {"password_hash": {"write_only": True}}

    # def validate_email(self, attrs):
    #     email = int(attrs['email'])
    #
    #     if email:
    #         emailset = Q(email__icontains=email)
    #         emailres = RegisterModel.objects.filter(email=email)
    #         if emailres:
    #             msg = _('The email address is already taken')
    #             raise serializers.ValidationError(msg)
    #         else:
    #             return attrs
    #

    def create(self, validated_data):
        return RegisterModel.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    user_name = serializers.CharField(
        max_length=255, min_length=3, read_only=True)

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = RegisterModel.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = RegisterModel
        fields = ['email', 'password', 'user_name', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        gender = attrs.get('gender', '')
        filtered_user_by_email = RegisterModel.objects.filter(email=email)
        user = auth.authenticate(email=email, password=password)
        user_data = RegisterModel.objects.get(email=email)
        active = user_data.is_active

        # if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
        #     raise AuthenticationFailed(
        #         detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)
        userdata = RegisterModel.objects.filter(email=email)
        print('------')
        print(userdata.get().email)
        print(userdata.get().is_active)
        gend = print(userdata.get().gender)
        if userdata.get().is_active:
            if not user:
                raise AuthenticationFailed({'data': '', 'message': 'invalid password',
                                            'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST})
            # elif:
            #     pass

            return {
                'email': user.email,

                'tokens': user.tokens,

            }
        else:
            return super().validate(attrs)


''' creating serializer class for RegisterModel with named EmailVerificationSerializer
'''


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = RegisterModel
        fields = ['token']


''' creating serializer class for SessionModel with named 
SessionSerializers with below criteria '''


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=3)

    class Meta:
        fields = ['email']


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68)
    token = serializers.CharField(
        min_length=1, write_only=True)
    uidb64 = serializers.CharField(
        min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = RegisterModel.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed({'data': '', 'message': ' reset link is invalid', 'status': 'failed'},
                                           401)

            user.set_password(password)
            user.save()
            return user


        except Exception as e:
            raise AuthenticationFailed({'data': '', 'message': ' reset link is invalid', 'status': 'failed'},
                                       401)

class AddUserSerializers(serializers.ModelSerializer):
    # password = serializers.CharField(
    #     max_length=68, min_length=6, write_only=True)
    #email = serializers.EmailField(validators=[validate_email])

    # default_error_messages = {
    #     'user_name': 'The user_name should only contain alphanumeric characters'}
    user_name = serializers.CharField(
         max_length=68, min_length=6, write_only=True)

    class Meta:
        model = RegisterModel
        fields = (
            'id',
            'user_name',
            'email',
            'phone_number',
            'gender',
            'first_name',
            'last_name',
            
            

        )
   

        extra_kwargs = {"password_hash": {"write_only": True}}

    # def validate_email(self, attrs):
    #     email = int(attrs['email'])
    #GetCompanyUsersList
    #     if email:
    #         emailset = Q(email__icontains=email)
    #         emailres = RegisterModel.objects.filter(email=email)
    #         if emailres:
    #             msg = _('The email address is already taken')
    #             raise serializers.ValidationError(msg)
    #         else:
    #             return attrs
    #

    # def create(self, validated_data):
    #    return RegisterModel.objects.create_user(**validated_data)
    # print('user_name=',user_name)




class GetCompanyuserListSerializers(serializers.ModelSerializer):
    

    class Meta:
        model=RegisterModel
        fields =('email','first_name',
                 'last_name','company_name',
                 'user_name','gender',
                 'phone_number','role',)
        
class VrLoginSerializers(serializers.ModelSerializer):
    

    class Meta:
        model=RegisterModel
        fields =('vrcode',)
        
        
class DeleteUserSerializers(serializers.ModelSerializer):
    

    class Meta:
        model=RegisterModel
        fields =('email',)
        
class GetOneUserUserSerializers(serializers.ModelSerializer):
    

    class Meta:
        model=RegisterModel
        fields =('email',)
                
class GetCompanyUsersListSerializers(serializers.ModelSerializer):
    

    class Meta:
        model=RegisterModel
        fields =('company_name',)
        
class Generatevrcodeserializers(serializers.Serializer):
    email = serializers.EmailField(min_length=3)

    class Meta:
        fields = ('email',)
        
class GetAllUsersSerializers(serializers.Serializer):
    

    class Meta:
        fields ="__all__"


class UpdateUserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(
    #     max_length=68, min_length=6, write_only=True)
    # email = serializers.EmailField(validators=[validate_email])

    default_error_messages = {
        'user_name': 'The user_name should only contain alphanumeric characters'}

    class Meta:
        model = RegisterModel
        fields = (
            # 'id',
            'user_name',
            'role',
           
            'gender',

        )

        # extra_kwargs = {"password_hash": {"write_only": True}}
