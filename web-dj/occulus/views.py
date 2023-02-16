from cgitb import reset
from django.shortcuts import render
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket
from rest_framework.response import Response
from .models import Oculus 
from .serializers import OculusSerializers
from rest_framework import status, generics, views
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import time
sender_address = 'support@xrconnect.io'
sender_pass = 'support@!23'
socket.getaddrinfo('localhost', 8080)
if __name__ == '__main__':
    pass


# Create your views here.
class  addOculus(generics.GenericAPIView):
       serializer_class = OculusSerializers
       permission_classes=(IsAuthenticated,)
       def post(self, request):
           if request.method=="POST":
            startime=time.time()
            try:
                res = request.data
                serializer = OculusSerializers(data=res)
                print(res)
                if serializer.is_valid():
                    serializer.save()
                    endtime=time.time()
                    return Response(
                        {'message': 'occulus saved successfully', 'status': 'success','Time taken':endtime - startime, 'code': status.HTTP_201_CREATED, })
                else:
                    return Response({'error': serializer.errors, 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST})



            except KeyError:
                return Response({'message': 'error',
                                'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)

        
           
            
            
        
        