
from django.shortcuts import render

from .models import Video, Comment


def home(request):
    search_query = ""

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    searched_videos = Video.objects.filter(title__icontains = search_query)
    viedos = Video.objects.all()
    
    context = {"videos":viedos,"searched_videos":searched_videos, "search_query":search_query}
    return render(request, "videos/home.html", context)


def video(request, pk):

    video = Video.objects.get(id=pk)
    video_list = Video.objects.all()
    video_list = video_list.exclude(id = pk)
    print(video)
    comments = Comment.objects.filter(video=video)
    context = {"video":video, "comments":comments, "video_list":video_list}
    return render(request, "videos/video.html", context)