
from django.contrib import admin
from django.urls import path,include
from .views import login,register,Saludo
urlpatterns = [
    path('saludo/',Saludo),
    path("login",login),
    path("register",register)

]
