
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.contrib.auth.models import User




def login_user(request):

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password )
        print(user)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "E-mail or password is incorrect")
            



    form = UserCreationForm
    context = {"form":form}
    return render(request, "users/login_register.html", context)