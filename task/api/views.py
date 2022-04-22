from task.models import Task
from django.shortcuts import HttpResponse
import json


def task_list(request):
    if request.method == "GET":
        task_list = Task.objects.all()
        tasks = [item.to_dict() for item in task_list]
        return HttpResponse(json.dumps(tasks))
    else:
        return HttpResponse(json.dumps('method not allowed'), status=405)