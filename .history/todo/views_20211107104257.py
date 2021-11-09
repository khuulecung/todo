from django.db.models import query
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin 
from .forms import CreateTaskForm
from .models import Task
from django.urls import reverse_lazy, reverse

# Create your views here.
class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = 'todo/create_task.html'
    form_class = CreateTaskForm
    model = Task
    login_url = '/login/'

    def get_success_url(self):
        return reverse("todo:task-list")

    def form_valid(self, form):
        return super().form_valid(form)

class TaskListView(LoginRequiredMixin, ListView):
    template_name = 'todo/task_list.html'
    model = Task
    context_object_name = "tasks"