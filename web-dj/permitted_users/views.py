from cgitb import reset
from django.shortcuts import render
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket
from rest_framework.response import Response
from .models import PermittedUsers as PermittedUserModel
from .serializers import PermittedUsersSerializers,GetContentSerializers
from rest_framework import status, generics, views
import time
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import PermittedUsersSerializers
sender_address = 'support@xrconnect.io'
sender_pass = 'support@!23'
socket.getaddrinfo('localhost', 8080)
if __name__ == '__main__':
    pass


# Create your views here.
class  PermittedUsers(generics.GenericAPIView):
       serializer_class = PermittedUsersSerializers
       permission_classes=(IsAuthenticated,)
       def post(self, request):
         startime=time.time()
         try:
            
            res = request.data
            serializer = PermittedUsersSerializers(data=res)
            print(res)
            if serializer.is_valid():
                serializer.save()
                endtime=time.time()
                
                return Response(
                    {'message': 'record saved successfully', 'status': 'success','Time taken':endtime - startime, 'code': status.HTTP_201_CREATED, })
            else:
                return Response({'error': serializer.errors, 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST})



         except KeyError:
            return Response({'message': 'error',
                             'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)
            
class GetContent (generics.GenericAPIView):
    serializer_class = GetContentSerializers
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        if request.method== "POST":
            startime=time.time()
            try:
                content = request.data['session_id']
                
                data = PermittedUserModel.objects.filter(session_id=content)
                if data:
                    serializers = PermittedUsersSerializers(data, many=True)
                    endtime=time.time()
                    return Response({'status': 'success', 'code': status.HTTP_200_OK, 'Time taken':endtime - startime,'content': serializers.data},
                                    status=status.HTTP_200_OK)
                else:
                    error = {'error': 'invalid session_id '}
                return Response({'message': error, 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)
            except KeyError:
                return Response({'status': 'failed', 'message': 'session_id ',
                                'code': status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)

             
               
            

             
        
           
            
            
        
        