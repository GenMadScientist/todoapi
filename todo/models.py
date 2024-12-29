from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

# Create your models here.
class Todo(models.Model):
    user =  models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name='todo')
    todo_list = models.CharField(max_length=30)
    title = models.CharField(max_length=20,unique=True)
    description = models.TextField()
    date_due = models.DateTimeField(default=datetime.today)
    image = models.ImageField(default="cafe.jpg")

    def __str__(self):
        return f'{self.id}({self.title})'
    
class Profile(models.Model):
    user = models.OneToOneField(User,default=1,on_delete=models.CASCADE, related_name='profile')
    DOB = models.DateField(auto_now_add=True)
    age = models.PositiveIntegerField()
    occupation = models.CharField(max_length=30)
    marital_status = models.CharField(max_length=20)
    address = models.CharField(max_length=20,blank=True,null=True) 
    about_me = models.TextField(blank=True, null=True)
    
class Like(models.Model):
    todo = models.ForeignKey(Todo,on_delete=models.CASCADE,related_name='likes')
    user = models.ForeignKey(User,default=1,on_delete=models.CASCADE,related_name='likes')
    date_liked = models.DateTimeField(default=datetime.now)

