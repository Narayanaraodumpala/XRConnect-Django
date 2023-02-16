from rest_framework.views import APIView

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import Session_mediaSerializers,GetOneSessionMediaSerializers,DeleteOneSessionMediaSerializers
from rest_framework.response import Response
import time
from .models import Session_Media as SessionMediaModel
from rest_framework import generics
''' list  all session_media data records    from   sessionmediamodel '''


class GetAllSessionMedia(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request):
        startime=time.time()
        queryset = SessionMediaModel.objects.all()
        serializers = Session_mediaSerializers(queryset, many=True)
        endtime=time.time()
        return Response({'status': 'success', 'code': status.HTTP_200_OK,'Time taken':endtime - startime, 'data': serializers.data},
                        status=status.HTTP_200_OK)


''' list  one session_media data  based  on session_id from   sessionmediamodel '''


class GetOneSessionMedia(generics.GenericAPIView):
    serializer_class = GetOneSessionMediaSerializers
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        if request.method=="POST":
            startime=time.time()
            try:
                session_id = request.data['session_id']
                res = SessionMediaModel.objects.get(session_id=session_id)
                if res:
                    dta = Session_mediaSerializers(res)
                    endtime=time.time()
                    return Response({'status': 'success', 'code': status.HTTP_200_OK, 'Time taken':endtime - startime,'session': dta.data},
                                    status=status.HTTP_200_OK)
                else:
                    return Response(
                        {'message': 'invalid session id', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                        status=status.HTTP_400_BAD_REQUEST)
            except SessionMediaModel.DoesNotExist:
                return Response({'message': 'invalid session id', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)
            except KeyError:
                return Response(
                    {'message': 'session id field is required', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                    status=status.HTTP_400_BAD_REQUEST)


''' delete  one session_media data  based session_id from   sessionmediamodel '''


class DeleteOneSessionMedia(generics.GenericAPIView):
    serializer_class = DeleteOneSessionMediaSerializers
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        if request.method=="POST":
            startime=time.time()
            try:

                session_id = request.data['session_id']
                res = SessionMediaModel.objects.filter(session_id=session_id).delete()
                if res[0] != 0:
                    endtime=time.time()
                    return Response(
                        {'status': 'success', 'message': 'media deleted successfully','Time taken':endtime - startime, 'code': status.HTTP_200_OK},
                        status=status.HTTP_200_OK)
                else:
                    return Response(
                        {'message': 'invalid session id', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                        status=status.HTTP_400_BAD_REQUEST)
            except KeyError:
                return Response(
                    {'message': 'session id field is required', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                    status=status.HTTP_400_BAD_REQUEST)


''' creating a session media into sessionmediamodel  when the session media  data is clear , if it's 
clear create , else return error message to users '''


class SessionMedia(generics.GenericAPIView):
    serializer_class = Session_mediaSerializers
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        if request.method=="POST":
            startime=time.time()
            data = request.data
            serializers = Session_mediaSerializers(data=data)
            if serializers.is_valid():
                serializers.save()
                endtime=time.time()
                return Response({'message': 'sessionmedia saved successfully',
                                'status': 'success','Time taken':endtime - startime, 'code': status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'message': serializers.errors, 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                    status=status.HTTP_400_BAD_REQUEST)
