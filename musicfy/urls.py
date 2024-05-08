
from django.contrib import admin
from django.urls import path,include
from .views import Saludo,UserView
from rest_framework import routers
router = routers.DefaultRouter()

# aqui registrare mi userView para que sea una ruta
router.register(r'user',UserView,'user')


urlpatterns = [
    path('saludo/',Saludo)
]
