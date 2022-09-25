from django.shortcuts import render

from .models import Video

def home(request):
    viedos = Video.objects.all()
    context = {"videos":viedos}
    return render(request, "videos/home.html", context)
