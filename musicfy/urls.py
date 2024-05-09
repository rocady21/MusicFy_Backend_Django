
from django.contrib import admin
from django.urls import path,include
from .views import login,register,Saludo,example_view,UserView,filter_user_by_name,send_friend_request,acept_friend_request,delete_friend_request,friend_requests_user,list_friends
from rest_framework import routers
router = routers.DefaultRouter()

# aqui registrare mi userView para que sea una ruta
router.register(r'user',UserView,'user')


urlpatterns = [
    path('saludo/',Saludo),
    path("login",login),
    path("register",register),
    path("valid_token",example_view),
    path("",include(router.urls)),
    path("users/<str:value>/",filter_user_by_name),
    path("user/friend_request/send",send_friend_request),
    path("user/friend_request/accept",acept_friend_request),
    path("user/friend_request/delete",delete_friend_request),
    path("user/friend_request",friend_requests_user),
    path("user/friends",list_friends),
]
