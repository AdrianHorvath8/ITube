from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("video/<str:pk>/", views.video, name="video"),
    path("subscriped_videos/", views.subscriped_videos, name="subscriped_videos"),

    path("like_video/<str:pk>/", views.like_video, name="like_video"),
    path("dislike_video/<str:pk>/", views.dislike_video, name="dislike_video"),
    path("remove_like_video/<str:pk>/", views.remove_like_video, name="remove_like_video"),
    path("remove_dislike_video/<str:pk>/", views.remove_dislike_video, name="remove_dislike_video"),
    path("history", views.history, name="history"),
    path("history_remove/<str:pk>/", views.history_remove, name="history_remove"),
]