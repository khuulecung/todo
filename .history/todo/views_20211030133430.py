from django.shortcuts import render
from django.views.generic.edit import CreateView, ListView
from .forms import CreateTaskForm
from .models import Task

# Create your views here.
class CreateTaskView(CreateView):
    template_name = 'create_task.html',
    form_class = CreateTaskForm,
    success_url = '',

    def form_valid(self, form):
        return super().form_valid(form)

class TaskListView(ListView):
    template_name = 'task_list.html',
    model = Task