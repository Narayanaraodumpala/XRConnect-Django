from pickletools import uint1
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class PermittedUsers (models.Model):
    date_created=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now_add=True)
    user_email=models.CharField(max_length=1000)
    session_id=models.CharField(max_length=100,unique=True)
    media_id=models.CharField(max_length=256)
    content_id=models.CharField(max_length=30,unique=True)
    
    class Meta:
        db_table='PermittedUsers'
        
    def __str__(self) :
        return self.user_email