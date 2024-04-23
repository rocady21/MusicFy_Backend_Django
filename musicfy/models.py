from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,BaseUserManager
# Create your models here.


class Rol(models.Model):
    name = models.TextField(max_length=50)

    def __str__(self):
        return self.name
    
class UserManager(BaseUserManager):
    def create_user(self,name,last_name,email,password,is_active,creae_user,id_rol,usuario_administrador):
        if not email and password:
            raise ValueError("El usuario debe de tener email y password")
        usuario = self.model(
            name = name,
            last_name = last_name,
            email = self.normalize_email(email),
            is_active = is_active,
            creae_user = creae_user,
            id_rol = id_rol,
        )

        usuario.set_password(password)
        usuario.save()
        return usuario
    def create_superuser(self,name,last_name,email,password,is_active,creae_user,id_rol,usuario_administrador):
        usuario = self.create_user(
            name = name,
            last_name = last_name,
            email = email,
            is_active = is_active,
            creae_user = creae_user,
            id_rol = id_rol,
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario

class User(AbstractBaseUser):
    name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    password = models.TextField(max_length=1000, unique=True)
    is_active = models.BooleanField(default=True)
    create_user = models.DateTimeField(auto_now=True)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE,related_name='users',null = True)
    usuario_administrador = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'last_name', 'password']  # Campos requeridos aparte del email y la contraseña

    objects = UserManager()

    def __str__(self):
        return f"{self.name} {self.last_name}"
    
    def has_perm(self,perm,obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador

class Status(models.Model):
    name = models.TextField(max_length=50)
    def __str__(self):
        return self.name

class Friends(models.Model): 
    id_from = models.ForeignKey(User, related_name="user_send_requeest" ,on_delete=models.CASCADE,null = True)
    id_to = models.ForeignKey(User, related_name="user_recive_requeest", on_delete=models.CASCADE,null = True)
    id_status = models.ForeignKey(Status,on_delete=models.CASCADE,null = True)

    def __str__(self):
        return self.id_from.name + " friend of" + self.id_to.name 




class PlayList_User(models.Model):
    from Playlist.models import Playlist

    id_playlist = models.ForeignKey(Playlist,on_delete=models.CASCADE,null = True)
    id_user = models.ForeignKey(User,on_delete=models.CASCADE,null = True)

    def __str__(self):
        return self.id_playlist.name + " from the user::" + self.id_user.name
    

class Like_playlist(models.Model):
    from Playlist.models import Playlist

    id_playlist = models.ForeignKey(Playlist,on_delete=models.CASCADE,null = True)
    id_user = models.ForeignKey(User,on_delete=models.CASCADE,null = True)

    def __str__(self):
        return self.id_user.name + " like to" + self.id_playlist.name

