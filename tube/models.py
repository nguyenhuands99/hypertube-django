from django.db import models


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255)


class Video(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField()


class VideoTag(models.Model):
    tag = models.ForeignKey(Tag, related_name='tag', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, related_name='video', on_delete=models.CASCADE)
