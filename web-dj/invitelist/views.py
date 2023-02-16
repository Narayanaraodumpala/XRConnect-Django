from cgitb import reset
from django.shortcuts import render
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket
import time
from rest_framework.response import Response
from .models import InviteeList
from rest_framework import status, generics, views
from .serializers import inviteEmailSerializers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
sender_address = 'support@xrconnect.io'
sender_pass = 'support@!23'
socket.getaddrinfo('localhost', 8080)
if __name__ == '__main__':
    pass


# Create your views here.
class  inviteEmail(generics.GenericAPIView):
    serializer_class = inviteEmailSerializers
    permission_classes=(IsAuthenticated,)
    def post(self, request):
     if request.method=="POST":
        startime=time.time()
        try:
             
                email=list(request.data['invite_email'].split(",")) 
                sessionid=request.data['session_id']
                if sessionid:
                    invite_link = 'https://demo.xrconnect.com/web/login'
                    for email in email:
                        re_email=email
                        print(re_email)
                        reciver_mail = re_email
                        message = MIMEMultipart()
                        message['From'] = sender_address
                        message['To'] = reciver_mail
                        message['Subject'] = 'invite to event! '
                        mail_content = 'hello' + ' ' + reciver_mail + ' please click this below  link to join event ' \
                                                                        '\n ' + invite_link
                        message.attach(MIMEText(mail_content, 'plain'))
                        s = smtplib.SMTP('smtp.gmail.com', 587)
                        s.starttls()
                        s.login(sender_address, sender_pass)
                        text = message.as_string()
                        s.sendmail(sender_address, reciver_mail, text)
                        s.quit()
                        InviteeList.objects.create(invite_email=email,session_id=sessionid,invite_link=invite_link)
                        endtime=time.time()
                    return Response({
                            'status': 'success', 'message': ' invite sent to email','Time taken':endtime - startime, 'code': status.HTTP_201_CREATED},
                            status=status.HTTP_201_CREATED)
                else:
                    return Response({'message': 'missing sessionid', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)
                    
        except KeyError:
            return Response({'message': 'missing data', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)
         
            

             
        
           
            
            
        
        