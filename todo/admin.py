from django.contrib import admin
from todo.models import Todo,Profile,Like

# Register your models here.
admin.site.register(Todo)
admin.site.register(Profile)
admin.site.register(Like)