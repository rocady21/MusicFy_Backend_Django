from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
# para crear una api en mi backend
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializer import UserSerializer
from .models import User,Status
from datetime import timedelta,timezone,datetime
from django.db.models import Q
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
from rest_framework import viewsets

# modelviewsets lo que hace es crear un CRUD con la clase que le pase 
class UserView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


def Saludo(request):

    return HttpResponse("A")
    



