
from django.shortcuts import render, redirect

from .models import Video, Comment
from users.models import Profile
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import CommentForm

def home(request):
    search_query = ""
    

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    searched_videos = Video.objects.filter(title__icontains = search_query)
    viedos = Video.objects.all().order_by("?")

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
    video_list = video_list.order_by("?")[:20]
    video.views.add(request.user.profile)
    profile = video.owner
    comments = Comment.objects.filter(video=video).order_by("-created")
    
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = request.user.profile
            comment.video = video
            comment.save()
            return redirect("video", pk=video.id)



    context = {"video":video, "comments":comments, "video_list":video_list, "form":form, "profile":profile}
    return render(request, "videos/video.html", context)


def subscriped_videos(request):
    following = request.user.profile.following.all()
    subscriped_profiles = Profile.objects.filter(id__in=[user.profile.id for user in following])
    viedos = Video.objects.filter(owner__in=[owner for owner in subscriped_profiles])
    

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
    
    context = {"videos":viedos,}
    return render(request, "videos/subscriptions.html", context)


def like_video(request, pk):
    video = Video.objects.get(id = pk)

    if request.user.profile in video.dislike.all():
        video.dislike.remove(request.user.profile)

    video.like.add(request.user.profile)
    return redirect(request.GET["next"] if "next" in request.GET else "posts")

def dislike_video(request, pk):
    video = Video.objects.get(id = pk)

    if request.user.profile in video.like.all():
        video.like.remove(request.user.profile)

    video.dislike.add(request.user.profile)
    
    return redirect(request.GET["next"] if "next" in request.GET else "posts")

def remove_like_video(request, pk):
    video = Video.objects.get(id = pk)
    video.like.remove(request.user.profile)
    
    return redirect(request.GET["next"] if "next" in request.GET else "posts")

def remove_dislike_video(request, pk):
    video = Video.objects.get(id = pk)
    video.dislike.remove(request.user.profile)
    
    return redirect(request.GET["next"] if "next" in request.GET else "posts")