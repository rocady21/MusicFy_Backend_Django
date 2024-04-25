# un serializer convierte los datos de py en un objeto json
# tambien nos hace validaciones, es decir si pasamos un obj con datos faltantes a los de field, nos da error 
# instanciar a serializer, es lo mismo que instanciar al modelo User, por ejemplo puedo crear datos con el serializer o con el propio modelo de user
from rest_framework import serializers
from .models import Friends,Rol,Status,User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","name" ,"last_name" ,"email" , "photo" ,"password" ,"is_active" ,"create_user" ,"id_rol"]
        
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ["id" ,"name"]

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ["id" ,"name"]

class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = ["id","id_from","id_to"]

