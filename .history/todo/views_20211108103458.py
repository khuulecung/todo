from django.db import models
from django.db.models import query
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin 
from .forms import CreateTaskForm
from .models import Task
from django.urls import reverse_lazy, reverse

# Create your views here.
class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = 'todo/task_create.html'
    form_class = CreateTaskForm
    model = Task
    login_url = '/login/'

    def get_success_url(self):
        return reverse("todo:task-list")

    def form_valid(self, form):
        task = form.save(commit=False)
        task.organization = self.request.user.userprofile
        task.save()

        return super().form_valid(form)

class TaskListView(LoginRequiredMixin, ListView):
    template_name = 'todo/task_list.html'
    model = Task
    context_object_name = "tasks"
    login_url = '/login/'


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'todo/task_update.html'
    model = Task
    form_class = CreateTaskForm

    def get_success_url(self):
        return reverse("todo:task-list")

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task