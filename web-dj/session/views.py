# import all packages and references which are needed for business logic development  in login views

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from .serializers import SessionSerializers,GetPrivateSessionsSerializers,GetOneSerializers,DeleteSessionSerializers
from rest_framework.response import Response
from .models import Session as SessionModel
import time
from django.db import IntegrityError
import socket

# declaring sender email address and password for sending token once users resister successfully..

sender_address = 'support@xrconnect.io'
sender_pass = 'support@!23'
socket.getaddrinfo('localhost', 8080)
if __name__ == '__main__':
    pass

''' creating a session when the session data is clear , if it's 
clear create , else return error message to users '''


class CreateSession(generics.GenericAPIView):
    serializer_class = SessionSerializers
    permission_classes=(IsAuthenticated,)
    
    
    def post(self, request):
        if request.method=="POST":
            try:
                startime=time.time()
                res = request.data
                serializer = SessionSerializers(data=res)
                print(res)
                if serializer.is_valid():
                    serializer.save()
                    endtime=time.time()
                    return Response(
                        {'message': 'session saved successfully', 'status': 'success','Time taken':endtime - startime, 'code': status.HTTP_201_CREATED, })
                else:
                    return Response({'error': serializer.errors, 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST})



            except KeyError:
                return Response({'message': 'error',
                                'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)


''' list  one session data  based on session_id from   AddSessionModel '''


class GetOneSession(generics.GenericAPIView):
    serializer_class = GetOneSerializers

    permission_classes=(IsAuthenticated,)
    
    def post(self, request):
        if request.method=="POST":
            startime=time.time()
            try:
                session = request.data['session_id']
                print(session)
                result = SessionModel.objects.get(session_id=session)
                if result:
                    serializer = SessionSerializers(result)
                    endtime=time.time()
                    return Response({'status': 'success', 'code': status.HTTP_200_OK,'Time taken':endtime - startime, 'data': serializer.data},
                                    status=status.HTTP_200_OK)
            except SessionModel.DoesNotExist:
                return Response({'message': 'invalid session id', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)
            except KeyError:
                return Response(
                    {'message': 'session id field is required', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                    status=status.HTTP_400_BAD_REQUEST)


class GetPrivateSessions(generics.GenericAPIView):
    serializer_class = GetPrivateSessionsSerializers
    permission_classes=(IsAuthenticated,)
    

    def post(self, request):
        if request.method=="POST":
            startime=time.time()
            try:
                private_email = request.data['host_user_email']
                private_sessions = SessionModel.objects.filter(host_user_email=private_email, access_type=1)
                public_session_data = SessionModel.objects.filter(access_type=0)
                # data = AddSessionModel.objects.values_list('invited_emails')
                # s_data = AddSessionModel.objects.values_list( 'session_id', 'event_name')

                private_sessions = SessionSerializers(private_sessions, many=True)

                public_sessions = SessionSerializers(public_session_data, many=True)

                sessionsList = private_sessions.data + public_sessions.data
                endtime=time.time()
                return Response({'status': 'success',
                                'code': status.HTTP_200_OK,'Time taken':endtime - startime,
                                #  'sessions': [serializers_data.data, public_session_serializer_data.data],
                                'sessions': sessionsList,
                                },
                                status=status.HTTP_200_OK)
            except KeyError:
                return Response({'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST,
                                'message': 'host_user_email field is required'})

    # def get(self,request):
    #        invited_emails = request.data['invited_emails']
    #
    #        data = AddSessionModel.objects.values_list('invited_emails')
    #        res=SessionsSerializers(data,many=True)

    # def get(self, request):
    #     startime=time.time()
    #     emails = request.data['invited_emails']
    #     print('requested email =', emails)
    #     l1 = []

    #     data = SessionModel.objects.filter(invited_emails__contains=emails)
    #     # for emails in data:
    #     #     l1.append(emails)
    #     #     print('list=', l1)
    #     # else:
    #     #     print('sorry')

    #     serializers_data = SessionSerializers(data, many=True)
    #     endtime=time.time()

    #     return Response({'status': 'success',
    #                      'code': status.HTTP_200_OK,'Time taken':endtime - startime,
    #                      'sessions': serializers_data.data,
    #                      },
    #                     status=status.HTTP_200_OK)


''' deleting  one session data  based on session_id from   session model '''


class DeleteSession(generics.GenericAPIView):
    serializer_class = DeleteSessionSerializers
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        if request.method=="POST":
            startime=time.time()
            try:
                session_id = request.data['session_id']
                session = SessionModel.objects.filter(session_id=session_id).delete()
                if session[0] != 0: 
                    endtime=time.time()
                    return Response(
                        {'status': 'success', 'message': 'user deleted successfully','Time taken':endtime - startime, 'code': status.HTTP_200_OK},
                        status=status.HTTP_200_OK)

                else:
                    return Response(
                        {'message': 'invalid session id', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                        status=status.HTTP_400_BAD_REQUEST)
            except KeyError:
                return Response(
                    {'message': 'session id field is required', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                    status=status.HTTP_400_BAD_REQUEST)


''' list all sessions from session model  '''


class GetAllSessions(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request):
        startime=time.time()
        queryset = SessionModel.objects.all()
        serializers = SessionSerializers(queryset, many=True)
        endtime=time.time()
        return Response({'status': 'success', 'code': status.HTTP_200_OK,'Time taken':endtime - startime, 'data': serializers.data},
                        status=status.HTTP_200_OK)
