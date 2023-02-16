# import your packages for writing and creating your database models for login app
from django.db import models

# Create your models here.


''' creating model for adding   content  with named  ContentModel with below fields  '''


class Contents(models.Model):
    content_id = models.CharField(max_length=256)
    content_name = models.CharField(max_length=256)
    content_type = models.CharField(max_length=256)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True,)
    thumbnail_path = models.CharField(max_length=256,default='')
    description = models.TextField()
    owner = models.CharField(max_length=256)
    access_type = models.CharField(max_length=256)
    file_path = models.CharField(max_length=300)
    file_name = models.CharField(max_length=256)
    version = models.CharField(max_length=256)
    build_target = models.CharField(max_length=200)
    uploaded_by = models.CharField(max_length=256,default='')

    def __str__(self):
        return self.content_name
    class Meta:
        db_table = 'Contents'
    
   


