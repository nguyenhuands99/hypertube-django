from django.urls import path

from .views import TubeView, MyLoginView, MySignupView


app_name = 'tube'

urlpatterns = [
    path('tube/', TubeView.as_view()),
    path('login/', MyLoginView.as_view()),
    path('signup/', MySignupView.as_view()),
]
