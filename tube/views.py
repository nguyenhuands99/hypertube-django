from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
from django.db.models import Q


from .models import Tag, Video, VideoTag

# Create your views here.

class TubeView(ListView):
    model = Video
    template_name = 'tube.html'
    context_object_name = 'videos'

    def get_queryset(self):
        q_query = self.request.GET.get('q', '')
        tag_query = self.request.GET.get('tag', '')
        if q_query:
            all_videos = Video.objects.filter(title__icontains=q_query)
        elif tag_query:
            tags = VideoTag.objects.filter(tag__name=tag_query)
            all_videos = [tag.video for tag in tags]
        else:
            all_videos = Video.objects.all()
        return all_videos


