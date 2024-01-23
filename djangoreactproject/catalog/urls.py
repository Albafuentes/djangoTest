from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name='login'),
]