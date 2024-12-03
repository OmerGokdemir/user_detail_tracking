from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Album(models.Model):
    userId = models.OneToOneField(User, models.CASCADE)
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.title}"
    

class Photo(models.Model):
    albumId = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="photos")
    title = models.CharField(max_length=255)
    url = models.ImageField(upload_to="images/")
    
    def __str__(self):
        return f"{self.title}"
    

