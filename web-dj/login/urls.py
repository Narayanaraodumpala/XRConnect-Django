from . import views
from django.urls import path, include
from .views import VerifyEmail, RegisterView, GetAllUsers, \
    PasswordTokenCheckAPi, RequestPasswordResetEmail, SetNewpASSWORDApiview,AddUser,\
        GetCompanyUsersList,Getuserpaginationlist,Generatevrcode,Vrlogin
# from login.models import SessionModel
# from  rest_framework.routers import  DefaultRouter
# router=DefaultRouter()
# router.register('SessionModel',Session,basename=SessionModel)
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # path('', views.index, name='index'),
    path('login', views.LoginAPIView.as_view(), name='login'),
    path('signup', RegisterView.as_view(), name='signup'),
    path('email-verify', VerifyEmail.as_view(), name="email-verify"),

    path('get_all_users', GetAllUsers.as_view(), name='all_users'),
    path('get_one_user', views.GetOneUser.as_view(), name='one_user'),
    path('delete_user', views.DeleteUser.as_view(), name='delete_user'),
    path('update_user', csrf_exempt(views.UpdateUser.as_view()), name='update_user'),
    path('passwpord-request-reset-email', RequestPasswordResetEmail.as_view(), name='request-reset-email'),
    path('reset-password/<uidb64>/<token>', PasswordTokenCheckAPi.as_view(), name='password-reset-confirm'),
    path('password-reset-confirm', SetNewpASSWORDApiview.as_view(), name='password-reset-confirm'),
    path('adduser',AddUser.as_view(),name='adduser'),
    path('getCompanyUsersList',GetCompanyUsersList.as_view(),name='getCompanyUsersList'),
    path('getuserpaginationlist',Getuserpaginationlist.as_view({'get': 'list'}),name='getuserpaginationlist'),
    path('generatevrcode',Generatevrcode.as_view(),name='generatevrcode'),
    path('vrlogin',Vrlogin.as_view(),name='vrlogin')

]
