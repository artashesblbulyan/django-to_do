from task.models import Task
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from task.serializers import TaskSerializer


@api_view(["GET"])
@renderer_classes([JSONRenderer])
def get_tasks(request):
    task_list = Task.objects.all()
    serialized_objects = TaskSerializer(task_list, many=True)

    return Response(serialized_objects.data)