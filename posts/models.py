from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    userId = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    
    def __str__(self):
        return f"{self.title}"
    

class Comment(models.Model):
    postId = models.OneToOneField(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField(max_length=1000)
    
    def __str__(self):
        return f"{self.name}"
