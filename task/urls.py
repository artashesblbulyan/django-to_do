from django.urls import path
from task.views import task as task_view
from task.views import task_api as task_api_view

urlpatterns = [
    path('', task_view.home, name="task_create"),
    path('tasks/', task_view.list_task, name="list_task"),
    path('tasks/<int:task_id>/', task_view.task_view, name="task_view"),
    path('tasks/<int:task_id>/update/', task_view.task_update, name="task_update"),
    path('tasks/<int:task_id>/delete/', task_view.task_delete, name="task_delete"),
]

api_urls = [
    path('api/tasks', task_api_view.get_tasks),
]

urlpatterns += api_urls