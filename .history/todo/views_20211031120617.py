from django.db.models import query
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import CreateTaskForm
from .models import Task

# Create your views here.
class CreateTaskView(CreateView):
    template_name = 'todo/create_task.html'
    form_class = CreateTaskForm
    model = Task
    success_url = 'task-list'

    def form_valid(self, form):
        return super().form_valid(form)

class TaskListView(ListView):
    template_name = 'todo/task_list.html'
    model = Task
    context_object_name = "tasks"