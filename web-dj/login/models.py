# import your packages for writing and creating your database models for login app
import datetime

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

''' Base-users model manager for Register model with named MyAccountManager '''


class MyAccountManager(BaseUserManager):
    def create_user(self, user_name, email, gender, password=None):
        if user_name is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(user_name=user_name, gender=gender,
                          email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, user_name, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(user_name, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


# AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
#                   'twitter': 'twitter', 'email': 'email'}
#
# ''' creating AbstractBaseUsermod for register the users with RegisterModel with below fields  '''


# class RegisterModel(AbstractBaseUser):
#     id = models.BigAutoField(primary_key=True)
#     user_name = models.CharField(max_length=128, null=True)
#     email = models.CharField(max_length=128, unique=True)
#     password = models.CharField(max_length=128, null=True)
#     gender = models.CharField(max_length=20, )
#     is_active = models.BooleanField(default=False)
#     # login_status = models.BooleanField(default=False)
#     company_name = models.CharField(max_length=128, default='xrconnect-client')
#     role = models.CharField(max_length=30, null=True, default='user')
#     # token = models.CharField(max_length=30,null=True)
#     # system_ID = models.CharField(max_length=30, null=True)
#     # login_status = models.BooleanField(default=False)
#     last_login = models.DateTimeField(auto_now_add=True, null=True)
#
#     # auth_provider = models.CharField(
#     #     max_length=255, blank=False,
#     #     null=False, default=AUTH_PROVIDERS.get('email'))
#     USERNAME_FIELD = 'email'
#
#     objects = MyAccountManager()

class RegisterModel(AbstractBaseUser):
        id = models.BigAutoField(primary_key=True)
        user_name = models.CharField(max_length=128, null=True)
        email = models.CharField(max_length=128, unique=True)
        password = models.CharField(max_length=128,null=True)
        gender = models.CharField(max_length=20, )
        is_active = models.BooleanField(default=False)
        first_name=models.CharField(max_length=128,null=True)
        last_name= models.CharField(max_length=128,null=True)
        phone_number=models.CharField(max_length=10,null=True)
        vrcode=models.CharField(max_length=10,null=True)
        
        # login_status = models.BooleanField(default=False)
        company_name = models.CharField(max_length=128, default='xrconnect-client',null=True)
        role = models.CharField(max_length=30, null=True, default='user')
        # token = models.CharField(max_length=30,null=True)
        # system_ID = models.CharField(max_length=30, null=True)
        # login_status = models.BooleanField(default=False)
        last_login = models.DateTimeField(auto_now_add=True, null=True)

        # auth_provider = models.CharField(
        #     max_length=255, blank=False,
        #     null=False, default=AUTH_PROVIDERS.get('email'))
        USERNAME_FIELD = 'email'

        objects = MyAccountManager()

        def tokens(self):
            refresh = RefreshToken.for_user(self)
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }

        class Meta:
            db_table = "users"

        def __str__(self):
            return str(self.email)

        def has_perm(self, perm, obj=None): return self.is_active

        def has_module_perms(self, app_label): return self.is_active


