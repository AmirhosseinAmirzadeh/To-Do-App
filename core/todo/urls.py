from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo-list'),
    path('create/', views.TodoCreateView.as_view(), name='todo-create'),
    path('<int:pk>/complete/', views.TodoCompleteView.as_view(), name='todo-complete'),
    path('<int:pk>/update/', views.TodoUpdateView.as_view(), name='todo-update'),
    path('<int:pk>/delete/', views.TodoDeleteView.as_view(), name='todo-delete'),
]