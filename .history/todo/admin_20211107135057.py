from django.contrib import admin
from .models import Task, User, UserProfile, Member

# Register your models here.
admin.site.register(Task)
admin.site.register(User)
admin.site.register(UserProfile)
