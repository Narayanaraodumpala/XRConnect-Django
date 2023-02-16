from cgitb import reset
from django.shortcuts import render
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket
import time
from rest_framework.response import Response
from .models import ContentAccess as  ContentAccessModel
from .serializers import ContentAccessSerializers
from rest_framework import status, generics, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
sender_address = 'support@xrconnect.io'
sender_pass = 'support@!23'
socket.getaddrinfo('localhost', 8080)
if __name__ == '__main__':
    pass


# Create your views here.
class  ContentAccess(generics.GenericAPIView):
      serializer_class = ContentAccessSerializers
      permission_classes=(IsAuthenticated,)
      def post(self, request):
        if request.method == "POST":
           startime=time.time()
           try:
                res=request.data
             
                serializers=ContentAccessSerializers(data=res)
                if serializers.is_valid():
                    email=list(request.data['invite_email'].split(","))
                    content_id=request.data['content_id']
                    for email in email:
                        re_email=email
                        print(re_email)
                    
                        ContentAccessModel.objects.create(invite_email=email,content_id=content_id)
                        endtime=time.time()
                    return Response({
                        'status': 'success', 'message': ' content saved','Time taken':endtime - startime, 'code': status.HTTP_201_CREATED},
                        status=status.HTTP_201_CREATED)
                else:
                    return Response({
                'status': 'failed', 'message': serializers.errors, 'code': status.HTTP_400_BAD_REQUEST},
                status=status.HTTP_400_BAD_REQUEST)
                    
           except KeyError:
            return Response({'message': 'missing data', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)
         

                    
         
                
                    
                        
                        
                   
               