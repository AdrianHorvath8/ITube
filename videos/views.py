from django.shortcuts import render

from .models import Video

def home(request):
    viedos = Video.objects.all()
    context = {"videos":viedos}
    return render(request, "videos/home.html", context)


def video(request, pk):

    video = Video.objects.get(id=pk)
    context = {"video":video}
    return render(request, "videos/video.html", context)