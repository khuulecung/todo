from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_organizor = models.BooleanField(default=True)
    is_member = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)

def post_task_created_signal(sender, instance, created, **kwargs):
    if created:
        Task.objects.create(organization=instance)
    print(instance)

post_save.connect(post_task_created_signal, sender=Task)