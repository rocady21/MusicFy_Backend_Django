from django.contrib import admin
from .models import Friends,Like_playlist,PlayList_User,Rol,Status,User
# Register your models here.

admin.site.register(Friends)
admin.site.register(Like_playlist)
admin.site.register(PlayList_User)
admin.site.register(Rol)
admin.site.register(Status)
admin.site.register(User)