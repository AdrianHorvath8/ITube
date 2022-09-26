from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("video/<str:pk>/", views.video, name="video")
]