from rest_framework import serializers
from .models import InviteeList
class inviteEmailSerializers(serializers.ModelSerializer):
    

    class Meta:
        model=InviteeList
        fields =('invite_email','session_id')