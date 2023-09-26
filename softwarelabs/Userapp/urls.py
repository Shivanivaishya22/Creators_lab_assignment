
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path("Singup" , views.Signup),
    path("Login" , views.Login),
    path("signout" , views.Logout) ,
] 
