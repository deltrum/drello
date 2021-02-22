from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.AddTask, name="add_task"),
    path('task/<int:pk>/', views.DeleteTask, name="delete_task"),
    path('taskmove/<int:pk>/', views.ChangeColumnTask, name="change_column_task"),
    path('tasks/<int:pk>/', views.Tasks, name="tasks"),
    path('taskcolumns/', views.TaskColumns, name="task_columns"),
]
