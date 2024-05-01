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
from .serializer import UserSerializer,FriendsSerializer
from .models import User,Friends,Status
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
        
        expiry_date = datetime.now() + timedelta(minutes=5)

    # Establece la fecha de expiración del token
        token.created = expiry_date
        token.save()

        if check_password(data["password"], user_date.data["password"]):
            return Response({
                "ok":True,
                "msg": "El user existe",
                "user": user_date.data,
                "token": token.key
            })
        else:
            return Response({
                "ok": False,
                "msg": "password incorrect"
            }, status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({
            "msg": "el correo no existe"
        })
    
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):


    data_user = UserSerializer(request.user)

    return Response({
        "ok":True,
        "msg":"autorizado con " + request.user.name,
        "data":data_user.data
    })
    
@api_view(["GET"])
def filter_user_by_name(request,value):

    filter_users = User.objects.filter(name__icontains=value).values()

    def filter_user_info(item):
        serialize_data = UserSerializer(item)
        
        return serialize_data.data

    result = list(map(lambda item: filter_user_info(item),filter_users))

    if len(result) != 0:
        return Response({
            "ok":True,
            "users":result
        },status.HTTP_200_OK)
    else: 
        return Response({
            "ok":False,
            "msg":"no users by name"
        },status.HTTP_404_NOT_FOUND)


# api for send friend_request to user
@api_view(["POST"])
def send_friend_request(request):

    data = request.data

    new_friend_request = FriendsSerializer(data=request.data)
    if new_friend_request.is_valid() :
        request_exist = Friends.objects.filter(id_from = new_friend_request.data["id_from"],id_to = new_friend_request.data["id_to"]).first()
        if not request_exist:
            # creo una nueva solicitud de amistad con id= 2
            user_from = User.objects.filter(id=new_friend_request.data["id_from"]).first()
            user_to = User.objects.filter(id=new_friend_request.data["id_to"]).first()
            status_request = Status.objects.get(id=2)   

            if user_from and user_to:
                
                new_friend = Friends(id_from = user_from, id_to = user_to,id_status = status_request)
                new_friend.save()

                return Response({
                    "ok":True,
                    "msg":"Solicitud de amistad enviada"
                },status.HTTP_200_OK)
        else: 
                return Response({
                    "ok":True,
                    "msg":"Ya existe una solicitud de amistad"
                },status.HTTP_200_OK)
        

    return Response({
                "ok":False,
                "msg":"Error en la solicitud"
            },status.HTTP_404_NOT_FOUND)
    
# api for send friend_request to user
@api_view(["PUT"])
def acept_friend_request(request):

    new_friend_request = FriendsSerializer(data=request.data)
    status_accpent = Status.objects.get(id=1)
    if new_friend_request.is_valid():
        # search request
        friend = Friends.objects.filter(id_from = new_friend_request.data["id_from"],id_to = new_friend_request.data["id_to"]).first()

        if friend: 
            friend.id_status = status_accpent
            friend.save()
            # return id_from 
            user = User.objects.filter(id= new_friend_request.data["id_from"]).first()
            user_data_serializer = UserSerializer(user)

            return Response({
                "ok":True,
                "msg":"Solicitud aceptada correctamente",
                "new_friend":user_data_serializer.data
            },status.HTTP_200_OK)
        else : 
            return Response({
                "ok":False,
                "msg":"No existe esa solicitud de amistad"
            },status.HTTP_400_BAD_REQUEST)
        

@api_view(["DELETE"])
def delete_friend_request(request):

    new_friend_request = FriendsSerializer(data=request.data)
    status_accpent = Status.objects.get(id=1)
    if new_friend_request.is_valid():
        # search request
        friend = Friends.objects.filter(id_from = new_friend_request.data["id_from"],id_to = new_friend_request.data["id_to"]).first()

        if friend: 
            friend.id_status = status_accpent
            friend.delete()

            return Response({
                "ok":True,
                "msg":"Eliminada correctamente"
            },status.HTTP_200_OK)
        else : 
            return Response({
                "ok":False,
                "msg":"No existe esa solicitud de amistad"
            },status.HTTP_400_BAD_REQUEST)
        
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def friend_requests_user(request):
    
    id_user = request.user.id
    status_request = Status.objects.get(id=2)

    print("status",status_request)

    Friends_request_user = Friends.objects.filter(id_to = id_user , id_status = status_request).all()
    

    friend_requests_data = []
    for friend_request in Friends_request_user:
        s_data = FriendsSerializer(friend_request)
        
        data = s_data.data

        friend_data = User.objects.filter(id=data["id_from"]).first()

        if friend_data:
            friend_serializer = UserSerializer(friend_data)
            data_user = friend_serializer.data

            data = {
                "id":data_user["id"] ,
                "name": data_user["name"],
                "last_name": data_user["last_name"] ,
                "photo": data_user["photo"],
                "is_active": data_user["is_active"] ,
                "id_rol": data_user["id_rol"]
            }
            friend_requests_data.append(data)

    if len(friend_requests_data):
        return Response({
            "ok":True,
            "msg":"hay solicitudes",
            "data":friend_requests_data
        },status.HTTP_200_OK)
    else:
        return Response({
            "ok":False,
            "msg":"No tienes solicitud de amistad"
        },status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_friends(request):
    
    id_user = request.user.id
    status_request = Status.objects.get(id=1)

    print("status",status_request)

    friends_user = Friends.objects.filter(Q(id_from = id_user) | Q(id_to = id_user) , id_status = status_request).all()
    
    friend_requests_data = []
    for friend_request in friends_user:
        s_data = FriendsSerializer(friend_request)
        
        data = s_data.data

        friend_data = User.objects.filter(id=data["id_from"]).first()

        if friend_data:
            friend_serializer = UserSerializer(friend_data)
            data_user = friend_serializer.data

            data = {
                "id":data_user["id"] ,
                "name": data_user["name"],
                "last_name": data_user["last_name"] ,
                "photo": data_user["photo"],
                "is_active": data_user["is_active"] ,
                "id_rol": data_user["id_rol"]
            }
            friend_requests_data.append(data)

    if len(friend_requests_data):
        return Response({
            "ok":False,
            "msg":"hay amigos",
            "data":friend_requests_data
        },status.HTTP_200_OK)
    else:
        return Response({
            "ok":False,
            "msg":"No hay amigos"
        },status.HTTP_400_BAD_REQUEST)



