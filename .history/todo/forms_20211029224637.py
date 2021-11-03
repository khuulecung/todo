from django import forms
from django.forms import fields
from .models import Task

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = (
            'title',
            'description',
            'due_date',
        )