import datetime

from django.db import models

# Create your models here.

''' creating model for adding sessions  with named  SessionModel with below fields  '''


class Session(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=128, unique=True)
    event_name = models.CharField(max_length=128, unique=True)
    event_type = models.CharField(max_length=128)
    parent_event_name = models.CharField(max_length=128)
    session_status = models.CharField(max_length=128)
    access_type = models.CharField(max_length=128)
    max_users = models.CharField(max_length=10)
    # invited_emails = models.CharField(max_length=1000,null=True,blank=True)s
    host_user_email = models.EmailField(null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.CharField(max_length=1000)
    environment_id = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    # content = models.CharField(max_length=1000)

    def __str__(self):
        return self.event_name
    class Meta:
        db_table = 'Sessions'









