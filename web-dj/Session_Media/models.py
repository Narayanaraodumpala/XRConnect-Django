from django.db import models

# Create your models here.

''' creating model for adding sessions  with named  Session_Media with below fields   '''


class Session_Media(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=128, unique=True)
    media_id = models.CharField(max_length=128)
    media_type = models.CharField(max_length=128)
    media_path = models.CharField(max_length=1028)

    def __str__(self):
        return self.media_path
    class Meta:
        db_table = 'Session_Media'
