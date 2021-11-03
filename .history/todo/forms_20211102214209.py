from django import forms
from django.forms import fields
from .models import Task

class DateInput(forms.)

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'due_date',
        )