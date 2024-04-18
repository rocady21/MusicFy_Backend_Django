from django.db import models
# Create your models here.


class Rol(models.Model):
    name = models.TextField(max_length=50)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.TextField(max_length=50)
    is_active = models.BooleanField(default=False)
    create_user = models.DateTimeField(auto_now=True)
    id_rol = models.ForeignKey(Rol,on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + self.last_name

class Status(models.Model):
    name = models.TextField(max_length=50)
    def __str__(self):
        return self.name

class Friends(models.Model): 
    id_from = models.ForeignKey(User, related_name="user_send_requeest" ,on_delete=models.CASCADE)
    id_to = models.ForeignKey(User, related_name="user_recive_requeest", on_delete=models.CASCADE)
    id_status = models.ForeignKey(Status,on_delete=models.CASCADE)

    def __str__(self):
        return self.id_from.name + " friend of" + self.id_to.name 

class Type_message(models.Model):
    name = models.TextField(max_length=100)
    def __str__(self):
        return self.name

class Messages(models.Model):
    id_from = models.ForeignKey(User, related_name="user_send_msgt", on_delete=models.CASCADE)
    id_to = models.ForeignKey(User, related_name="user_recibe_msg", on_delete=models.CASCADE)
    message = models.TextField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)
    id_type_message = models.ForeignKey(Type_message,on_delete=models.CASCADE)

    def __str__(self):
        return self.message 

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
    gender_id = models.ForeignKey(Gender,on_delete=models.CASCADE)

    def __str__(self):
        return self.title 

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
    id_song = models.ForeignKey(Song,on_delete=models.CASCADE)
    id_playlist = models.ForeignKey(Playlist,on_delete=models.CASCADE)

    def __str__(self):
        return self.id_song.title + " from playlist:" + self.id_playlist.name

class PlayList_User(models.Model):
    id_playlist = models.ForeignKey(Playlist,on_delete=models.CASCADE)
    id_user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.id_playlist.name + " from the user::" + self.id_user.name
    

class Like_playlist(models.Model):
    id_playlist = models.ForeignKey(Playlist,on_delete=models.CASCADE)
    id_user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.id_user.name + " like to" + self.id_playlist.name

class Playlist_gender(models.Model):
    id_gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
    id_playlist = models.ForeignKey(Playlist,on_delete=models.CASCADE)
    def __str__(self):
        return self.id_playlist + " have gender: " + self.id_gender.name

class Artist_song(models.Model):
    id_song = models.ForeignKey(Song,on_delete=models.CASCADE)
    id_user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.id_song.title + " from the artist :" + self.id_user.name