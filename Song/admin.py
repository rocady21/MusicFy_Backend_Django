from django.contrib import admin
from .models import  Gender,Song,Artist_song

# Register your models here.
admin.site.register(Gender)
admin.site.register(Song)
admin.site.register(Artist_song)
