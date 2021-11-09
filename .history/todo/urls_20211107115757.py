from django.urls import path
from .views import CreateTaskView, TaskListView, TaskUpdateView

app_name = "todo"

urlpatterns = [
    path('', TaskListView.as_view(), name="task-list"),
    path('create/', CreateTaskView.as_view(), name="task-create"),
    path('update/', UpdateTaskView.as_view(), name="task-update"),
]
