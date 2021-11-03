from django import forms
from django.forms import fields, DateField, widgets
from .models import Task

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'due_date',
        )
        exclude = ()
        widgets = {
            'order_date'
        }