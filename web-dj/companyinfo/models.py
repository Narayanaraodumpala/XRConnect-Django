from pickletools import uint1
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class  Companyinfo(models.Model):
    date_created=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now_add=True)
    company_id=models.CharField(max_length=1000,primary_key=True)
    company_name=models.CharField(max_length=100,unique=True)
    ceo_name=models.CharField(max_length=256)
    email=models.EmailField(unique=True)
    number=models.CharField(max_length=10)
    website=models.CharField(max_length=100)
    address=models.CharField(max_length=256)
    status=models.CharField(max_length=30)
    technology=models.CharField(max_length=1000,default='IT')
    language=models.CharField(max_length=100,default='EN')
    #timezone=models.CharField(max_length=256)
    company_created_by=models.CharField(max_length=30)
    
    class Meta:
        db_table='Companyinfo'
        
    def __str__(self) :
        return self.company_name