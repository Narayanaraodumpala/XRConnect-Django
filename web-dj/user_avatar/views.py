import imp
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserAvtarSerializers,GetUserAvtarSerializers
from .models import Avatars
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated 
from rest_framework import status
import time
from rest_framework.response import Response
# Create your views here.
class UserAvatars(generics.GenericAPIView):
    serializer_class = UserAvtarSerializers
    permission_classes=(IsAuthenticated,)
    def post(self,request):
         if request.method=="POST":
            startime=time.time()
            data=request.data
            serializers=UserAvtarSerializers(data=data)
            if serializers.is_valid():
                serializers.save()
                endtime=time.time()
                return Response({'status': 'success', 'message': 'avatar uploaded successfully','Time taken':endtime - startime,
                                'code': status.HTTP_201_CREATED},
                                status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'status': 'failed', 'message': serializers.errors, 'code': status.HTTP_400_BAD_REQUEST},
                    status=status.HTTP_400_BAD_REQUEST)
                
class Get_avatar(generics.GenericAPIView):
    serializer_class = GetUserAvtarSerializers
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        if request.method=="POST":
            startime=time.time()
            try:
                user = request.data['user_id']
                resp = Avatars.objects.filter(user_id=user)
                if resp:
                    data = UserAvtarSerializers(resp, many=True)
                    endtime=time.time()
                    return Response({'status': 'success','Time taken':endtime - startime, 'code': status.HTTP_200_OK, 'avatar': data.data},
                                    status=status.HTTP_200_OK)
                else:
                    return Response(
                        {'status': 'failed', 'message': 'invalid user id', 'code': status.HTTP_400_BAD_REQUEST},
                        status=status.HTTP_400_BAD_REQUEST)
            except KeyError:
                return Response(
                    {'message': 'user id field is required', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                    status=status.HTTP_400_BAD_REQUEST)
       
       