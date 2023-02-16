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

from content import views
from user_content.views import UserContent, GetAllUserContents, GetUserBuildtargetContent, GetOneUserContent

urlpatterns = [

    path('user_content', UserContent.as_view(), name='user_content'),
    path('get_all_user_contents', GetAllUserContents.as_view(), name='get_all_user_contents'),
    path('get_usercontent_buildtarget', GetUserBuildtargetContent.as_view(), name='get_usercontent_buildtarget'),
    path('get_one_usercontent', GetOneUserContent.as_view(), name='get_one_usercontent'),

]
