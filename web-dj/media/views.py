from rest_framework.views import APIView

from rest_framework import status

from .serializers import MediaSerializers,DeleteMediaSerializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Media as MediaModel
import time
import socket
from rest_framework import status, generics, views
sender_address = 'support@xrconnect.io'
sender_pass = 'support@!23'
socket.getaddrinfo('localhost', 8080)
if __name__ == '__main__':
    pass


class GetAllMedia(APIView):
    
    permission_classes=(IsAuthenticated,)
    def get(self, request):
        startime=time.time()
        queryset = MediaModel.objects.all()
        serializers = MediaSerializers(queryset, many=True)
        endtime=time.time()
        return Response({'status': 'success', 'code': status.HTTP_200_OK,'Time taken':endtime - startime, 'mediaList': serializers.data},
                        status=status.HTTP_200_OK)


''' delete  one media  data  based  on media_id from   metamodel '''


class DeleteMedia(generics.GenericAPIView):
    serializer_class = DeleteMediaSerializers
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        if request.method=="POST":
            startime=time.time()
            try:
                media_id = request.data['media_id']
                print('media id to delete',media_id)
                queryset = MediaModel.objects.filter(media_id=media_id).delete()
                if queryset[0] != 0:
                    endtime=time.time()
                    return Response(
                        {'status': 'success', 'message': 'media deleted successfully','Time taken':endtime - startime, 'code': status.HTTP_200_OK},
                        status=status.HTTP_200_OK)

                else:
                    return Response(
                        {'message': 'invalid media id', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                        status=status.HTTP_400_BAD_REQUEST)
            except KeyError:
                return Response(
                    {'message': 'media id field is required', 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                    status=status.HTTP_400_BAD_REQUEST)


class Media(generics.GenericAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = MediaSerializers

    def post(self, request):
        if request.method=="POST":
            startime=time.time()
            data = request.data
            serializer_class = MediaSerializers(data=data)
            if serializer_class.is_valid():
                serializer_class.save()
                endtime=time.time()
                return Response({'message': 'media uploaded successfully',
                                'status': 'success','Time taken':endtime - startime, 'code': status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'message': serializer_class.errors, 'status': 'failed', 'code': status.HTTP_400_BAD_REQUEST},
                    status=status.HTTP_400_BAD_REQUEST)
