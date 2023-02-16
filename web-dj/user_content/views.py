from django.shortcuts import render
# import all packages and references which are needed for business logic development  in content  views
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated                                                                                                                                                                                                                               
from .serializers import UserContentSerializers,GetUserBuildtargetContentSerializers,GetOneUserContenttSerializers
from .models import UserContentModel
import time
from rest_framework import generics

class UserContent(generics.GenericAPIView):
    serializer_class = UserContentSerializers
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        if request.method=="POST":
            startime=time.time()
            data = request.data
            serializers_class = UserContentSerializers(data=data)

            if serializers_class.is_valid():
                serializers_class.save()
                endtime=time.time()
                return Response({'status': 'success', 'message': 'user-content saved successfully','Time taken':endtime - startime,
                                'code': status.HTTP_201_CREATED},
                                status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'status': 'failed', 'message': serializers_class.errors, 'code': status.HTTP_400_BAD_REQUEST},
                    status=status.HTTP_400_BAD_REQUEST)


''' list all the GetAllUserContents which are present in UserContentModel model   '''


class GetAllUserContents(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request):   
        startime=time.time()
        queryset = UserContentModel.objects.all()
        serializers = UserContentSerializers(queryset, many=True)
        endtime=time.time()
        return Response({'status': 'success','Time taken':endtime - startime, 'code': status.HTTP_200_OK, 'content': serializers.data},
                        status=status.HTTP_200_OK)


''' list   one build_target data  based on build_target and content_id from UserContentModel   '''


class GetUserBuildtargetContent(generics.GenericAPIView):
    serializer_class=GetUserBuildtargetContentSerializers
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        if request.method=="POST":
            startime=time.time()
            try:
                content = request.data['content_id']
                buildtarget = request.data['build_target']
                data = UserContentModel.objects.filter(content_id=content, build_target=buildtarget)
                if data:
                    serializers = UserContentSerializers(data, many=True)
                    endtime=time.time()
                    return Response({'status': 'success', 'Time taken':endtime - startime,'code': status.HTTP_200_OK, 'content': serializers.data},
                                    status=status.HTTP_200_OK)
                else:
                    error = {'error': 'invalid build-target or content_id  '}
                return Response({'message': error, 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)
            except KeyError:
                return Response({'status': 'failed', 'message': 'content id and build_target both fields are required',
                                'code': status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)


''' list   OneUserContent record  based on content_id from   UserContentModel '''


class GetOneUserContent(generics.GenericAPIView):
    serializer_class=GetOneUserContenttSerializers
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        if request.method=="POST":
            startime=time.time()
            try:
                contid = request.data['content_id']
                resp = UserContentModel.objects.filter(content_id=contid)
                if resp:
                    data = UserContentSerializers(resp, many=True)
                    endtime=time.time()
                    return Response({'status': 'success','Time taken':endtime - startime, 'code': status.HTTP_200_OK, 'content': data.data},
                                    status=status.HTTP_200_OK)
                else:
                    return Response(
                        {'status': 'failed', 'message': 'invalid content id', 'code': status.HTTP_400_BAD_REQUEST},
                        status=status.HTTP_400_BAD_REQUEST)
            except KeyError:
                return Response(
                    {'message': 'content id field is required', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                    status=status.HTTP_400_BAD_REQUEST)
                
                
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#  import imp
# from django.shortcuts import render
# from rest_framework.views import APIView
# from .serializers import UserAvtarSerializers,GetUserAvtarSerializers
# from .models import Avatars
# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated 
# from rest_framework import status
# import time
# from rest_framework.response import Response
# # Create your views here.
# class UserAvatars(generics.GenericAPIView):
#     serializer_class = UserAvtarSerializers
#     permission_classes=(IsAuthenticated,)
#     def post(self,request):
#          if request.method=="POST":
#             startime=time.time()
#             data=request.data
#             serializers=UserAvtarSerializers(data=data)
#             if serializers.is_valid():
#                 serializers.save()
#                 endtime=time.time()
#                 return Response({'status': 'success', 'message': 'avatar uploaded successfully','Time taken':endtime - startime,
#                                 'code': status.HTTP_201_CREATED},
#                                 status=status.HTTP_201_CREATED)
#             else:
#                 return Response({
#                     'status': 'failed', 'message': serializers.errors, 'code': status.HTTP_400_BAD_REQUEST},
#                     status=status.HTTP_400_BAD_REQUEST)
                
# class Get_avatar(generics.GenericAPIView):
#     serializer_class = GetUserAvtarSerializers
#     permission_classes=(IsAuthenticated,)
#     def post(self, request):
#         if request.method=="POST":
#             startime=time.time()
#             try:
#                 user = request.data['user_id']
#                 resp = Avatars.objects.filter(user_id=user)
#                 if resp:
#                     data = UserAvtarSerializers(resp, many=True)
#                     endtime=time.time()
#                     return Response({'status': 'success','Time taken':endtime - startime, 'code': status.HTTP_200_OK, 'avatar': data.data},
#                                     status=status.HTTP_200_OK)
#                 else:
#                     return Response(
#                         {'status': 'failed', 'message': 'invalid user id', 'code': status.HTTP_400_BAD_REQUEST},
#                         status=status.HTTP_400_BAD_REQUEST)
#             except KeyError:
#                 return Response(
#                     {'message': 'user id field is required', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
#                     status=status.HTTP_400_BAD_REQUEST)
       
       
       
       
       
       
# urls.py 



# """xrconnect/content URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """

# from django.urls import path

# from content import views
# from .views import UserAvatars,Get_avatar
# from xrconnect import settings
# from django.conf.urls.static import static
# urlpatterns = [

#     path('useravatars/', UserAvatars.as_view(), name='useravatars'),
#     path('get_avatar/',Get_avatar.as_view(),name='get_avatar')
  
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
    
    
    
    
    
# serializers.py 


# # creating serializers for content app and models
# from rest_framework import serializers
# from .models import Avatars




# ''' creating serializer class for UserContentModel with named 
# UserContentSerializers with below criteria '''


# class UserAvtarSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Avatars
#         fields = [
#             'user_id',
#             'model_file_path',
           
#         ]
        
#     def create(self, validated_data):
#         return Avatars.objects.create(**validated_data)
    
# class GetUserAvtarSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Avatars
#         fields = [
#             'user_id',
           
           
#         ]
        




# models.py 



# from django.db import models

# # Create your models here.
# def user_directory_path(instance, filename):
    
# 	# file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
# 	return 'user_avatars'.format(instance.user.id, filename)

# class Avatars(models.Model):
#     user_id=models.CharField(max_length=128,unique=True)
#     model_file_path=models.FileField(upload_to=user_directory_path)
    
#     def __str__(self) :
#         return self.user_id
    
#     class Meta:
#         db_table='UserAvatar'
    
 

#  path('useravatras/',include('useravatars.urls')),
 
 
#   "useravatars",