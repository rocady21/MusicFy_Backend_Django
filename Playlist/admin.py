from django.contrib import admin
from .models import Playlist,Playlist_songs,Playlist_gender
# Register your models here.
admin.site.register(Playlist)
admin.site.register(Playlist_songs)
admin.site.register(Playlist_gender)

