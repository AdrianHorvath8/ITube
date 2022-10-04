
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
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