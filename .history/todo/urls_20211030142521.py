from django.urls import path
from .views import CreateTaskView, TaskListView

app_name = "todo"

urlpatterns = [
    path('', TaskListView.as_view(), name="task-list"),
    path('create/', CreateTaskView.as_view(), name="task-create"),
]
