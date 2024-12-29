from django.db import models
from datetime import datetime
from todo.models import Todo
# Create your models here.

class Comments(models.Model):
    todo = models.ForeignKey(Todo,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=50)
    description = models.TextField()
    user = models.CharField(max_length=10)
    thumbsup = models.PositiveIntegerField(default=0)
    #successful = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=datetime.now)
    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return f'{self.id} - {self.name}'
"""
class Like(models.Model):
    comment = models.ForeignKey(Comments,default=1,on_delete=models.CASCADE,related_name='thumbups')
    time_stamp = models.DateTimeField(default=datetime.now)
    #date_created = models.DateTimeField(default=datetime.now)
"""