
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from users.models import Profile
from videos.models import Video
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User




def login_user(request):

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password )
        

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "E-mail or password is incorrect")
            
    
    return render(request, "users/login_register.html",)

def logout_user(request):
    logout(request)
    messages.success(request, "successfuly logout")
    return redirect("home")



def register(request):
    page = "register"
    form = RegisterForm()


    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():

            user = form.save()
            messages.success(request, "User successfuly created")
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Error during registration")
    
    
    context = {"form":form, "page":page}
    return render(request, "users/login_register.html", context)


def profile(request,pk):
    profile = Profile.objects.get(id=pk)
    videos = Video.objects.filter(owner=profile)
    context = {"profile":profile, "videos":videos}
    return render(request, "users/profile_page.html", context)

def subscribe(request, pk):
    profile = Profile.objects.get(id=pk)
    profile.followers.add(request.user)
    return redirect(request.GET["next"] if "next" in request.GET else "posts")


def unsubscribe(request, pk):
    profile = Profile.objects.get(id=pk)
    profile.followers.remove(request.user)
    return redirect(request.GET["next"] if "next" in request.GET else "posts")