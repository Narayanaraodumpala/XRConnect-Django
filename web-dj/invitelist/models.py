from django.db import models

# Create your models here.
class InviteeList(models.Model):
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    date_modified=models.DateTimeField(auto_now_add=True,null=True)
    invite_email=models.CharField(max_length=1000)
    session_id=models.CharField(max_length=100)
    invite_link=models.CharField(max_length=256)
    
    class Meta:
        db_table='InviteList'
        
    def __str__(self) :
        return self.session_id