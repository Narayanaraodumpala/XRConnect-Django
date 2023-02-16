# creating serializers for login app and models
from rest_framework import serializers

from .models import Oculus

''' creating serializer class for SessionModel with named 
SessionSerializers with below criteria '''


class OculusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Oculus
        fields = ('oculus_id',)
