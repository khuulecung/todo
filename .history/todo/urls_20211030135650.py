from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path('create_task/', views.CreateTaskView.as_view(), name="create-task"),
    path('task_list/', views.TaskListView.as_view(), name="create-task"),
]
