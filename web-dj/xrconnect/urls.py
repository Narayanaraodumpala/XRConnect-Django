"""xrconnect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, pathr
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include

# from .views import auth
from rest_framework import routers

schema_view = get_schema_view(
    openapi.Info(
        title="XRCONNECT - CLIENT APi",
        default_version='v3',
        description=" Note :- For authorised APIs, replace 'JWT Authorization header using the Bearer scheme' with the user's jwt token.After successfully logging in,place your access token  with Bearer key at Authorize value. <html><body><h4>For example : Bearer your access token </h3></body></html>",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@XRCONNECT.local"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
from rest_framework.schemas import get_schema_view

from rest_framework_simplejwt import views as jwt_views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,TokenRefreshView
    
)
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('login.urls')),

    path('content/', include('content.urls')),
    path('user_content/', include('user_content.urls')), 
    path('session/', include('session.urls')),
    path('media/', include('media.urls')),
    path('useravatras/',include('user_avatar.urls')),
    path('session_user/', include('session_user.urls')),
     path('invitelist/', include('invitelist.urls')),
    #path('session_media/', include('Session_Media.urls')),
    path('permitted_users/', include('permitted_users.urls')),
    path('occulus/', include('occulus.urls')),
    path('content_access/', include('content_access.urls')),
        path('company_info/', include('companyinfo.urls')),
       
    # path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    # path('api/token/refresh',TokenRefreshView.as_view(),name='token_refresh'),
     
path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
    #  path('openapi/', get_schema_view(
    #     title="School Service",
    #     description="API developers hpoing to use our service"
    # ), name='openapi-schema'),
    #   path('docs/', TemplateView.as_view(
    #     template_name='documents.html',
    #     extra_context={'schema_url':'openapi-schema'}
    # ), name='swagger-ui'),
    #  path('openapi/', TemplateView.as_view(template_name="index.html")),

]
 