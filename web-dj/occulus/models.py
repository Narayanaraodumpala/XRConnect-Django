from pickletools import uint1
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Oculus (models.Model):
    date_created=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now_add=True)
   
    oculus_id=models.CharField(max_length=100)
   
    
    class Meta:
        db_table='Oculus'
        
    def __str__(self) :
        return self.oculus_id