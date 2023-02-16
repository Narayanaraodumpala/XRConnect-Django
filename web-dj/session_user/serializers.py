# creating serializers for login app and models
from rest_framework import serializers

from .models import Session_Users

''' creating serializer class for Session_Users with named 
SessionUserSerializers with below criteria '''


class SessionUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Session_Users
        fields = "__all__"
