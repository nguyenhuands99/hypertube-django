from django.urls import path

from .views import TubeView


app_name = 'tube'

urlpatterns = [
    path('tube/', TubeView.as_view(), name='search_results'),
]
