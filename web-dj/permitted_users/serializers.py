# creating serializers for login app and models
from rest_framework import serializers

from .models import PermittedUsers

''' creating serializer class for SessionModel with named 
SessionSerializers with below criteria '''


class PermittedUsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = PermittedUsers
        fields = ('user_email', 'session_id', 'media_id', 'content_id')
        


class GetContentSerializers(serializers.ModelSerializer):
    class Meta:
        model = PermittedUsers
        fields = ( 'content_id',)
        