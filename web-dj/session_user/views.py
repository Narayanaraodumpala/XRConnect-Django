# import all packages and references which are needed for business logic development  in login views

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from rest_framework import status, generics


from rest_framework.response import Response
from rest_framework import generics
import socket
from rest_framework.permissions import IsAuthenticated
from .serializers import SessionUserSerializers
import time
sender_address = 'support@xrconnect.io' 
sender_pass = 'support@!23'
socket.getaddrinfo('localhost', 8080)
if __name__ == '__main__':
    pass


''' creating a session_user  into sessionusermodel  when the session data is clear , if it's 
clear create , else return error message to users '''


class SessionUsers(generics.GenericAPIView):
    serializer_class = SessionUserSerializers
    permission_classes=(IsAuthenticated,)
    def post(self, request):
         if request.method=="POST":
            startime=time.time()
            data = request.data
            serializer = SessionUserSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                endtime=time.time()
                return Response({'message': 'sessionuser saved successfully',
                                'status': 'success','Time taken':endtime - startime, 'code': status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'message': serializer.errors, 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                    status=status.HTTP_400_BAD_REQUEST)
