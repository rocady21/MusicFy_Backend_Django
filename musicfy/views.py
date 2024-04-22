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
from .models import User
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.


def Saludo(request):

    return HttpResponse("A")

@api_view(["POST"])
def register(request):
    
    data_user = request.data


    # valida el usaurio con el serializer
    serializer_user = UserSerializer(data=data_user)
    
    # encript password 

    if serializer_user.is_valid():
        email = serializer_user.validated_data.get("email")
        new_password = serializer_user._validated_data.get("password")
        password_encripted = make_password(new_password)
        serializer_user.validated_data["password"] = password_encripted
        
        if User.objects.filter(email=email).exists():
            return Response({
                "ok": False,
                "msg": "Ya existe un usuario con este email"
            }, 400)
        else:
            # save dataase
            user_instance = serializer_user.save()
            serializer_new_user = UserSerializer(user_instance)

            return Response({
                "msg":"usuario registrado correctamente",
                "user":serializer_new_user.data
            },400)
    else:
        return Response({
            "ok":False,
            "msg":"data from user no valid"
        },400)

@api_view(["POST"])
def login(request):
    data = request.data

    exist_user = User.objects.filter(email=data["email"]).first()

    if exist_user:
        user_date = UserSerializer(exist_user)
        user_id = user_date.data["id"]
        token, created = Token.objects.get_or_create(user_id=user_id)

        if check_password(data["password"], user_date.data["password"]):
            return Response({
                "msg": "El correo existe",
                "user": user_date.data,
                "token": token.key
            })
        else:
            return Response({
                "ok": False,
                "msg": "password incorrect"
            }, status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    else:
        return Response({
            "msg": "el correo no existe"
        })
    
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    print(request.user.is_active)

    return Response({
        "msg":"autorizado con " + request.user.name
    })
