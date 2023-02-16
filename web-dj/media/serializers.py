from rest_framework import serializers

from .models import Media

''' creating serializer class for Media with named 
MediaSerializers with below criteria '''


class MediaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['media_id', 'media_type', 'owner', 'uploaded_by', 'access_type','file_path']


class DeleteMediaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('media_id', )
