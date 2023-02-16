from django.db import models

# Create your models here.
def user_directory_path(instance, filename):
    
	# file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
	return 'user_avatar'.format(instance.user_id, filename)

class Avatars(models.Model):
    user_id=models.CharField(max_length=128,unique=True)
    model_file_path=models.FileField(upload_to=user_directory_path)
    
    def __str__(self) :
        return self.user_id
    
    class Meta:
        db_table='UserAvatar'