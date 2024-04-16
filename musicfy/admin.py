from django.contrib import admin
from .models import Artist_song,Friends,Gender,Like_playlist,Messages,Playlist,Playlist_gender,Playlist_songs,PlayList_User,Rol,Song,Status,Type_message,User
# Register your models here.

admin.site.register(Artist_song)
admin.site.register(Friends)
admin.site.register(Gender)
admin.site.register(Like_playlist)
admin.site.register(Messages)
admin.site.register(Playlist)
admin.site.register(Playlist_gender)
admin.site.register(Playlist_songs)
admin.site.register(PlayList_User)
admin.site.register(Song)
admin.site.register(Rol)
admin.site.register(Status)
admin.site.register(Type_message)
admin.site.register(User)