from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import CustomUserChangeForm, LoginForm, SignupForm


def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("tasks")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("tasks")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("login")


@login_required
def profile_update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("tasks")
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, "accounts/update_profile.html", {"form": form})
