from django.db import models
from django.db.models import query
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin 
from .forms import CreateTaskForm, SignUpForm
from .models import Task
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

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

    def get_queryset(self):
        user = self.request.user
        if user.is_organizor:
            queryset = Task.objects.filter(organization=user.userprofile, member__isnull=False)
        if user.is_member:
            queryset = Task.objects.filter(organization=user.member.organization, member__isnull=False)
            queryset = Task.objects.filter(member__user=user)
        return super().get_queryset()


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'todo/task_update.html'
    model = Task
    form_class = CreateTaskForm

    def get_success_url(self):
        return reverse("todo:task-list")

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'todo/task_delete.html'
    model = Task

    def get_success_url(self):
        return reverse("todo:task-list")

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse("login")