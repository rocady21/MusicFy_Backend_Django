# un serializer convierte los datos de py en un objeto json
# tambien nos hace validaciones, es decir si pasamos un obj con datos faltantes a los de field, nos da error 
# instanciar a serializer, es lo mismo que instanciar al modelo User, por ejemplo puedo crear datos con el serializer o con el propio modelo de user
from rest_framework import serializers
from .models import Artist_song,Friends,Gender,Like_playlist,Messages,Playlist,Playlist_gender,Playlist_songs,PlayList_User,Rol,Song,Status,Type_message,User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","name" ,"last_name" ,"email" ,"password" ,"is_active" ,"create_user" ,"id_rol"]
        
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ["id" ,"name"]

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ["id" ,"name"]

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id","title","desc","photo","url_song","duration","gender_id"]

class Type_MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_message
        fields = ["id" ,"name"]

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ["id","id_from","id_to","message","timestamp","id_type_message",]

class Like_playlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like_playlist
        fields = ["id,","id_playlist","id_user"]

class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = ["id","id_from","id_to","id_status"]

class Artist_songSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist_song
        fields = ["id","id_song","id_user"]


class Playlist_genderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist_gender
        fields = ["id","id_gender","id_playlist"]

class Playlist_songsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist_songs
        fields = ["id","id_song","id_playlist"]

class PlayList_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayList_User
        fields = ["id","id_playlist","id_user"]

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ["id","name"]

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ["id","name","duration_tot","num_songs","photo","desc","create_at","views","last_updated",]
