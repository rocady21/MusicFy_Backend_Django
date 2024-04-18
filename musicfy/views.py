from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
# para crear una api en mi backend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializer import UserSerializer
from .models import User
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


    if exist_user : 
        user_date = UserSerializer(exist_user)
        user_id = user_date.data["id"]
        token,created = Token.objects.get_or_create(user_id=user_id)
        if user_date.data["password"] == data["password"]:
            return Response({
                "msg":"El correo existe",
                "user":user_date.data,
                "token":token.key
            })
        else: 
            return Response({
                "ok":False,
                "msg":"password incorrect"
            },status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    else:
        return Response({
            "msg":"el correo no existe"
        })