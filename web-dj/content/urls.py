"""xrconnect/content URL Configuration

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
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .views import Content, Get_All_Content, Get_One_Content, Get_Buildtarget_Content, GetApplicationData, \
    GetEnvironmentData

urlpatterns = [
    path('upload_internal_content', Content.as_view(), name='content'),
    path('get_all_content', Get_All_Content.as_view(), name='get_all_content'),
    path('get_buildtarget_content', Get_Buildtarget_Content.as_view(), name='get_buildtarget_content'),
    path('get_one_content', Get_One_Content.as_view(), name='get_one_content'),

    path('get_environments_list', GetEnvironmentData.as_view(), name='get_environment_data'),
    path('get_applications_list', GetApplicationData.as_view(), name='get_application_data'),

]
