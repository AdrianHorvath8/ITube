from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("video/<str:pk>/", views.video, name="video"),
    path("subscriped_videos/", views.subscriped_videos, name="subscriped_videos"),
]