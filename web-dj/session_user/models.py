from django.db import models

# Create your models here.

''' creating model for adding sessions  with named  Session_Users with below fields  '''


class Session_Users(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    session_id = models.CharField(max_length=128)
    user_id = models.CharField(max_length=128)
    user_role = models.CharField(max_length=128)
    # user_avatar = models.CharField(max_length=1028)
    # is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.session_id
    class Meta:
        db_table = 'Session_Users'



