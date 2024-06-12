from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.


class Video(models.Model):
    video = models.FileField(upload_to='video', validators=[
        FileExtensionValidator(['mp4', 'WMV'])
    ])