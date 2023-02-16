# creating serializers for login app and models
from rest_framework import serializers

from .models import ContentAccess

''' creating serializer class for SessionModel with named 
SessionSerializers with below criteria '''


class ContentAccessSerializers (serializers.ModelSerializer):
    class Meta:
        model = ContentAccess
        fields = ('invite_email','content_id')
        

