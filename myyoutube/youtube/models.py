from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Video(models.Model):
    thumbnail = models.ImageField(upload_to='thumbnails')
    title = models.CharField(max_length=100)
    description = models.TextField()
    published_at = models.DateTimeField()

class Comment(models.Model):
    video = models.ForeignKey(Video,on_delete=models.CASCADE)
    text = models.TextField()
    published_at = models.DateTimeField()