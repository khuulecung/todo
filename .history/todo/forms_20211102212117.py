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
        widgets = {
            'start_date': DatePickerInput(), # default date-format %m/%d/%Y will be used
            'end_date': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
        }