from django import forms
from django.forms import fields
from .models import Task

# https://www.youtube.com/watch?v=I2-JYxnSiB0
# https://www.youtube.com/watch?v=UidskJk0KiE

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'due_date',
        )
        widgets = {
            'due_date': DateInput()
        }