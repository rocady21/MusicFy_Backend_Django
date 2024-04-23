from django.db import models
# Create your models here.
class Type_message(models.Model):
    name = models.TextField(max_length=100)
    def __str__(self):
        return self.name

class Messages(models.Model):
    from musicfy.models import User

    id_from = models.ForeignKey(User, related_name="user_send_msgt", on_delete=models.CASCADE, null = True)
    id_to = models.ForeignKey(User, related_name="user_recibe_msg", on_delete=models.CASCADE, null = True)
    message = models.TextField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)
    id_type_message = models.ForeignKey(Type_message,on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.message 