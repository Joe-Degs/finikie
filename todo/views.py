from rest_framework import generics

from todo.serializers import TaskSerializer
from todo.models import Task

class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer()