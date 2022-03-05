from django.urls import path
from task import views

urlpatterns = [
    path('', views.home, name="home"),
    path('tasks/', views.list_task, name="list_task"),
    path('tasks/update/<int:task_id>/', views.task_update, name="task_update"),
    path('tasks/<int:task_id>/', views.task_view, name="task_view"),
    path('tasks/<int:task_id>', views.task_delete, name="task_delete"),
]
