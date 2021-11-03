from django.shortcuts import render
from django.views.generic.edit import CreateView
from . import models

# Create your views here.
class CreateTaskView(CreateView)