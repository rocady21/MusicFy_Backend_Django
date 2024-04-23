from django.db import models

# Create your models here.
class Playlist(models.Model):
    name = models.TextField(max_length=100)
    duration_tot = models.IntegerField()
    num_songs = models.IntegerField()
    photo = models.TextField(max_length=500)
    desc = models.TextField(max_length=500)
    create_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    last_updated = models.DateTimeField()

    def __str__(self):
        return self.nane
    
class Playlist_songs(models.Model):
    from Song.models import Song

    id_song = models.ForeignKey(Song,on_delete=models.CASCADE, null = True)
    id_playlist = models.ForeignKey(Playlist,on_delete=models.CASCADE,null = True)

    def __str__(self):
        return self.id_song.title + " from playlist:" + self.id_playlist.name

class Playlist_gender(models.Model):
    from Song.models import Gender

    id_gender = models.ForeignKey(Gender,on_delete=models.CASCADE,null = True)
    id_playlist = models.ForeignKey(Playlist,on_delete=models.CASCADE,null = True)
    def __str__(self):
        return self.id_playlist + " have gender: " + self.id_gender.name