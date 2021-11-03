from django.urls import path
from .views import CreateTaskView, TaskListView

app_name = "todo"

urlpatterns = [
    path('create_task/', CreateTaskView.as_view(), name="task-create"),
    path('task_list/', TaskListView.as_view(), name="task-list"),
]
