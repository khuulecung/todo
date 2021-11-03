from django import forms

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = 