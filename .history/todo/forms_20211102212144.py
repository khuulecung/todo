from django import forms
from django.forms import fields
from .models import Task
from bootstrap_datepicker_plus import DatePickerInput

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
        }