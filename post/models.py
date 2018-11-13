from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    authorr = models.CharField(max_length=50, default='temp')
    time = models.DateField(auto_now_add=True)
    usernickname = models.CharField(max_length=50, default='temp')
    
    def __str__(self):
        return self.title
        
        