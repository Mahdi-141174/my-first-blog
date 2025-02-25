from django.urls import path
from . import views

urlpatterns = [
    path("welcome/", views.welcome, name="welcome"),
    path("", views.home, name="home"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("sign_in/", views.sign_in, name="sign_in"),
]
