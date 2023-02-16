# creating serializers for content app and models
from rest_framework import serializers
from .models import  UserContentModel




''' creating serializer class for UserContentModel with named 
UserContentSerializers with below criteria '''


class UserContentSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserContentModel
        fields = [
            'content_id',
            'content_name',
            'content_type',
            'content_load_type',
            'thumbnail_path',
            'description',
            'owner',
            'access_type',
            'path',
            'version',
            'file_name',
            'build_target'
        ]


class GetUserBuildtargetContentSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserContentModel
        fields = ('content_id',
            
            'build_target'
        )
            
class GetOneUserContenttSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserContentModel
        fields = ('content_id',
            
          
        )
            
