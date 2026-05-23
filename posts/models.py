from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.title[:15]