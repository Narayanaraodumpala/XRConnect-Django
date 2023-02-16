from django.db import models

# Create your models here.
''' creating model for adding   users content  with named  UserContentModel with below fields  '''


class UserContentModel(models.Model):
    content_id = models.CharField(max_length=128)
    content_name = models.CharField(max_length=528)
    content_type = models.CharField(max_length=128)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    content_load_type = models.CharField(max_length=150,null=True)
    thumbnail_path = models.CharField(max_length=500)
    description = models.TextField()
    owner = models.CharField(max_length=200)
    access_type = models.CharField(max_length=128)
    file_path = models.CharField(max_length=200)
    version = models.CharField(max_length=128)
    file_name = models.CharField(max_length=128)
    build_target = models.CharField(max_length=128)
    uploaded_by = models.CharField(max_length=256,default='')
    path=models.CharField(max_length=256,null=True,default=' ')
    def __str__(self):
        return self.content_name

    class Meta:
        db_table = "User_Contents"
