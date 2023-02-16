# creating serializers for login app and models
from rest_framework import serializers

from .models import Session_Media

''' creating serializer class for Session_Media with named 
Session_mediaSerializers with below criteria '''


class Session_mediaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Session_Media
        fields = "__all__"
        

class GetOneSessionMediaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Session_Media
        fields = ('session_id',)
        
class DeleteOneSessionMediaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Session_Media
        fields = ('session_id',)