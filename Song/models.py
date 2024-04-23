from django.db import models
# Create your models here.

    
class Gender(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name 


class Song(models.Model):
    title = models.TextField(max_length=100)
    desc = models.TextField(max_length=500)
    photo = models.TextField(max_length=500)
    url_song = models.TextField(max_length=500)
    duration = models.FloatField(default=0)
    gender_id = models.ForeignKey(Gender,on_delete=models.CASCADE,null = True)

    def __str__(self):
        return self.title 
    

class Artist_song(models.Model):
    from musicfy.models import User

    id_song = models.ForeignKey(Song,on_delete=models.CASCADE,null = True)
    id_user = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    def __str__(self):
        return self.id_song.title + " from the artist :" + self.id_user.name
