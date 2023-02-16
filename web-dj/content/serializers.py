# creating serializers for content app and models
from rest_framework import serializers
from .models import Contents

''' creating serializer class for ContentModel with named 
ContentSerializers with below criteria '''


class ContentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contents
        fields = [
            'content_id',
            'content_name',
            'content_type',
            'thumbnail_path',
            'description',
            'owner',
            'access_type',
            'file_path',
            'file_name',
            'version',
            'build_target',
            'uploaded_by'
        ]



class Get_Buildtarget_ContentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contents
        fields = [
            'content_id',
            
            'build_target',
            
        ]


class Get_One_ContentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contents
        fields = [
            'content_id',
            
          
            
        ]
