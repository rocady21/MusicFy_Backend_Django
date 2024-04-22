
from django.contrib import admin
from django.urls import path,include
from .views import login,register,Saludo,example_view
urlpatterns = [
    path('saludo/',Saludo),
    path("login",login),
    path("register",register),
    path("valid_token",example_view)
]
