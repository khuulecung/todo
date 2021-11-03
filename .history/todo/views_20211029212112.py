from django.shortcuts import render
from django.views.generic.edit import CreateView
from models import Task

# Create your views here.
class CreateTaskView(CreateView):
    model = Task
    fields = [
        'title',
        'description',
        'created_date',
        'due_date',
    ]

    def form_valid(self, form):
        return super().form_valid(form)