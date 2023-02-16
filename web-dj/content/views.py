from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Contents
from .serializers import ContentSerializers,Get_Buildtarget_ContentSerializers,Get_One_ContentSerializers
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticated
import time
from rest_framework import status, generics, views
""" creating a content record  into Contentmodel   when the content  data is clear , if it's 
clear create , else return error message to users """


class Content(generics.GenericAPIView):
    serializer_class=ContentSerializers
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        startime=time.time()
        try:
            internalContentDuplicates = Contents.objects.filter(
                content_id=request.data["content_id"],
                build_target=request.data["build_target"],
            ).all()
            
            if internalContentDuplicates:
                print("in if block:21")
                for contentName in internalContentDuplicates:
                   
                    Contents.objects.filter(
                        content_name=contentName,
                        build_target=request.data["build_target"],
                        content_id=request.data["content_id"],
                    ).delete()
            data = request.data
            serilaizers_class = ContentSerializers(data=data)
            if serilaizers_class.is_valid():
                serilaizers_class.save()
                endtime=time.time()
                return Response(
                    {
                        "data": "",
                        "message": "addressable uploaded successfully",
                        "status": "success",
                        "code": status.HTTP_201_CREATED,
                        'Time taken':endtime - startime,
                    },
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {
                        "status": "failed",
                        "message": serilaizers_class.errors,
                        "code": status.HTTP_400_BAD_REQUEST,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except IntegrityError as e:
            return Response(
                {
                    "status": "failed",
                    "message": "addressable existed with this content_id",
                    "code": status.HTTP_400_BAD_REQUEST,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


""" list all the Get_All_Content which are present in ContentModel model   """


class Get_All_Content(APIView):
    
    permission_classes=(IsAuthenticated,)
    def get(self, request):
        startime=time.time()
        queryset = Contents.objects.all()
        serializers = ContentSerializers(queryset, many=True)
        endtime=time.time()
        return Response(
            {
                "status": "success",
                "code": status.HTTP_200_OK,
                "contentsList": serializers.data,
                'Time taken':endtime - startime,
            },
            status=status.HTTP_200_OK,
        )


""" list   one buildtarget data  based on buildtarget and content_id from ContentModel   """


class Get_Buildtarget_Content(generics.GenericAPIView):
    serializer_class=Get_Buildtarget_ContentSerializers
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        startime=time.time()
        try:
            data = request.data["build_target"]
            content = request.data["content_id"]
            print(data)
            res = Contents.objects.filter(buildtarget=data)
            if res:
                serializers = ContentSerializers(res, many=True)
                endtime=time.time()
                return Response(
                    {
                        "status": "success",
                        "code": status.HTTP_200_OK,
                        "contentsList": serializers.data,
                        'Time taken':endtime - startime,
                    },
                    status=status.HTTP_200_OK,
                    
                )
            else:
                error = {"error": "invalid build-target or content_id"}
            return Response(
                {
                    "message": error,
                    "status": "failed",
                    "code": status.HTTP_400_BAD_REQUEST,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except KeyError:
            return Response(
                {
                    "status": "failed",
                    "message": "content id and build_target both fields are required",
                    "code": status.HTTP_400_BAD_REQUEST,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


""" list  one Content record  based on content_id from   ContentModel """


class Get_One_Content(generics.GenericAPIView):
    serializer_class=Get_One_ContentSerializers
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        startime=time.time()
        try:
            content = request.data["content_id"]

            print(content)
            res = Contents.objects.get(content_id=content)
            if res:
                response = ContentSerializers(res)
                endtime=time.time()
                return Response(
                    {
                        "status": "success",
                        "code": status.HTTP_200_OK,
                        "contentsList": response.data,
                        'Time taken':endtime - startime,
                    },
                    status=status.HTTP_200_OK,
                )

        except Contents.DoesNotExist:
            return Response(
                {
                    "message": "invalid content_id",
                    "status": "failed",
                    "code": status.HTTP_400_BAD_REQUEST,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except KeyError:
            return Response(
                {
                    "message": "content id field is required",
                    "status": "failed",
                    "code": status.HTTP_400_BAD_REQUEST,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


""" list   EnvironmentData record    ContentModel """


class GetEnvironmentData(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request):
        startime=time.time()
        data = Contents.objects.filter(content_type=1)
        response = ContentSerializers(data, many=True)
        endtime=time.time()
        return Response(
            {"status": "success", "code": status.HTTP_200_OK,'Time taken':endtime - startime, "envList": response.data},
            status=status.HTTP_200_OK,
        )


""" list   ApplicationData record    ContentModel """


class GetApplicationData(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request):
        startime=time.time()
        resp = Contents.objects.filter(content_type=2)
        response = ContentSerializers(resp, many=True)
        endtime=time.time()
        return Response(
            {
                "status": "success",
                "code": status.HTTP_200_OK,
                'Time taken':endtime - startime,
                "appsList": response.data,
            },
            status=status.HTTP_200_OK,
        )



