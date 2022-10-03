
from django.shortcuts import render

from .models import Video, Comment


def home(request):
    

    viedos = Video.objects.all()
    
    context = {"videos":viedos,}
    return render(request, "videos/home.html", context)


def video(request, pk):

    video = Video.objects.get(id=pk)
    video_list = Video.objects.all()
    video_list = video_list.exclude(id = pk)
    print(video)
    comments = Comment.objects.filter(video=video)
    context = {"video":video, "comments":comments, "video_list":video_list}
    return render(request, "videos/video.html", context)