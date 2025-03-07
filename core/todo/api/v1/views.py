from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .permissions import IsOwnerOrReadOnly
from .serializers import TodoSerializer
from todo.models import Todo
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class TodoModelViewset(viewsets.ModelViewSet):
    "A class for getting list and detail of Todo tasks"
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['complete']
    search_fields = ['title']
    ordering_fields = ['complete']
    
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Todo.objects.none()
        return Todo.objects.filter(user=self.request.user.profile)
    