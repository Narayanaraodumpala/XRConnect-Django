from django.db import models

# Create your models here.
class ContentAccess(models.Model):
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    date_modified=models.DateTimeField(auto_now_add=True,null=True)
    invite_email=models.CharField(max_length=1000)
    content_id=models.CharField(max_length=100)
    
    class Meta:
        db_table='ContentAccess'
        
    def __str__(self) :
        return self.invite_email