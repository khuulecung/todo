from django.shortcuts import render
from django.views.generic.edit import CreateView
from models import Task

# Create your views here.
class CreateTaskView(CreateView):
    template_name = '',
    form_

    def form_valid(self, form):
        return super().form_valid(form)