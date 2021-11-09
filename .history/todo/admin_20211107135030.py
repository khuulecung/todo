from django.contrib import admin
from .models import Task, User, UserProfile

# Register your models here.
admin.site.register(Task)
admin.site.register(User)
