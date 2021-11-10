from django import forms
from django.forms import fields
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

# https://www.youtube.com/watch?v=I2-JYxnSiB0
# https://www.youtube.com/watch?v=UidskJk0KiE

class DateInput(forms.DateInput):
    input_type = 'date' # https://www.w3schools.com/html/html_form_input_types.asp

class CheckboxInput(forms.CheckboxInput):
    input_type = 'checkbox'

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'due_date',
            'complete',
        )
        widgets = {
            'due_date': DateInput(),
            'complete': CheckboxInput(),
        }
        
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")