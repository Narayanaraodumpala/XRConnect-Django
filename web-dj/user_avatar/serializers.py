
# creating serializers for content app and models
from rest_framework import serializers
from .models import Avatars




''' creating serializer class for UserContentModel with named 
UserContentSerializers with below criteria '''


class UserAvtarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Avatars
        fields = [
            'user_id',
            'model_file_path',
           
        ]
        
    def create(self, validated_data):
        return Avatars.objects.create(**validated_data)
    
class GetUserAvtarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Avatars
        fields = [
            'user_id',
           
           
        ]
        
