from django import forms
from django.forms import fields
from . import models

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = (
            'title',
            ''
        )