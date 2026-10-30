from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "perfil.html")

def create_user(request):
    if request.method == "POST":
        if User.objects.filter(username=request.POST["username"]).exists():
            return render(request, "register.html", {"error_message": "Esse nome de usuário já existe"})
        # create_user já salva no banco e guarda a senha como hash
        User.objects.create_user(
            request.POST["username"],
            request.POST["email"],
            request.POST["password"],
        )
        return redirect("login")
    return render(request, "register.html")

def login_user(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user:
            login(request, user)
            return redirect("home")
        return render(request, "login.html", {"error_message": "Usuário não existe"})
    return render(request, "login.html")

def logout_user(request):
    logout(request)
    return redirect("login")
