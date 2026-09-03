from django.utils.http import MAX_URL_LENGTH
from django.db import models
from django.contrib.auth.models import User


class Videos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    caption = models.TextField()
    video = models.FileField(upload_to='videos/', blank=True, null=True)


    def __str__(self):
        return self.user.username

class likes(models.Model):
    user = models.OneToOneField(Videos, on_delete=models.CASCADE)
    
    

    def __str__(self):
        return self.user.username

class Comments(models.Model):
    user = models.OneToOneField(Videos, on_delete=models.CASCADE)
    comment = models.TextField()  
    
    
    def __str__(self):
        return self.user.username