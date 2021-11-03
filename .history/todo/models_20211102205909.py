from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank=True)

    def __str__(self):
        return self.title