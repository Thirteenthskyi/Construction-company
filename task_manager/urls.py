from django.urls import path

from task_manager.views import (
    index,
    ProjectListView,
    TaskListView,
    EmployeeListView,
    EmployeeDetailView,
    TaskDetailView
)

urlpatterns = [
    path("", index, name="index"),
    path("employees/", EmployeeListView.as_view(), name="employee-list"),
    path("employees/<int:pk>/", EmployeeDetailView.as_view(), name="employee-detail"),
    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>", TaskDetailView.as_view(), name="task-detail"),

]

app_name = "task_manager"
