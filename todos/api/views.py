from rest_framework import viewsets
from todos.models import Todo
from todos.api.serializers import TodoSerializer

class TodoModelViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer