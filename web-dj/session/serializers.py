# creating serializers for login app and models
from rest_framework import serializers

from .models import Session as SessionModel

''' creating serializer class for SessionModel with named 
SessionSerializers with below criteria '''


class SessionSerializers(serializers.ModelSerializer):
    class Meta:
        model = SessionModel
        fields = ('id', 'session_id', 'event_name', 'access_type', 'event_type', 'parent_event_name',
                  'max_users', 'host_user_email', 'description', 'environment_id', 'category',
                  'start_date', 'end_date', 'session_status')
        
class GetPrivateSessionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = SessionModel
        fields = ( 'host_user_email',)
        
class GetOneSerializers(serializers.ModelSerializer):
    class Meta:
        model = SessionModel
        fields = ( 'session_id',)
        
        
class DeleteSessionSerializers(serializers.ModelSerializer):
    class Meta:
        model = SessionModel
        fields = ( 'session_id',)


