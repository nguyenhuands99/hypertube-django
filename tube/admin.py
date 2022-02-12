from django.contrib import admin

from .models import Tag, Video, VideoTag
# Register your models here.

admin.site.register(Tag)
admin.site.register(Video)
admin.site.register(VideoTag)
