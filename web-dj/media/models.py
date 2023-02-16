from django.db import models


# Create your models here.
class Media(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    media_id = models.CharField(max_length=128, unique=True)
    media_type = models.CharField(max_length=128)
    # thumbnail_path = models.CharField(max_length=128,default='')
    # description = models.TextField()
    owner = models.CharField(max_length=128)
    uploaded_by = models.CharField(max_length=128)
    access_type = models.CharField(max_length=128)
    # permitted_users = models.CharField(max_length=128,default='')
    file_path = models.CharField(max_length=128)
    # version = models.CharField(max_length=128,default='')

    def __str__(self):
        return self.media_id
    class Meta:
        db_table = 'Media'
