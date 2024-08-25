from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from tasks.models import Task

from .serializers import TaskSerializer

@api_view(['GET'])
def task_list_view(request, *args, **kwargs):
    qs = Task.objects.all()
    serializer = TaskSerializer(qs, many=True)
    return Response(serializer.data)