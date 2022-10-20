
from django.shortcuts import render, redirect

from .models import Video, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import CommentForm

def home(request):
    search_query = ""
    

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    searched_videos = Video.objects.filter(title__icontains = search_query)
    viedos = Video.objects.all()

    page = request.GET.get("page")
    paginator = Paginator(viedos, 9)

    try:
        viedos = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        viedos = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        viedos = paginator.page(page)
    
    context = {"videos":viedos,"searched_videos":searched_videos, "search_query":search_query}
    return render(request, "videos/home.html", context)


def video(request, pk):

    video = Video.objects.get(id=pk)
    video_list = Video.objects.all()
    video_list = video_list.exclude(id = pk)
    video.views.add(request.user.profile)
    profile = video.owner

    
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = request.user.profile
            comment.video = video
            comment.save()
            return redirect("video", pk=video.id)

    
    comments = Comment.objects.filter(video=video)


    context = {"video":video, "comments":comments, "video_list":video_list, "form":form, "profile":profile}
    return render(request, "videos/video.html", context)