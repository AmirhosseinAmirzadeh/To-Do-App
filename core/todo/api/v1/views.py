from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .permissions import IsOwnerOrReadOnly
from .serializers import TodoSerializer
from todo.models import Todo

class TodoModelViewset(viewsets.ModelViewSet):
    "A class for getting list and detail of Todo tasks"
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TodoSerializer
    
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Todo.objects.none()
        return Todo.objects.filter(user=self.request.user.profile)
    