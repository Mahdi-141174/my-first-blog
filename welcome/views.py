from django.shortcuts import render


def welcome(request):
    return render(request, "welcome/welcome.html", {})


def home(request):
    return render(request, "welcome/home.html", {})


def sign_up(request):
    return render(request, "welcome/sign_up.html", {})


def sign_in(request):
    return render(request, "welcome/sign_in.html", {})


# Create your views here.
