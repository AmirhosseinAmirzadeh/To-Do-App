from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, View, UpdateView, DeleteView
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
import json

# Create your views here.
class TodoListView(LoginRequiredMixin, ListView):
    "A class for todo list"
    model = Todo
    context_object_name = 'tasks'
    template_name = 'todo/todo_list.html'
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user.profile)
    
    
class TodoCreateView(LoginRequiredMixin, CreateView):
    "A class to create todo"
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo:todo-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user.profile
        return super(TodoCreateView, self).form_valid(form)


class TodoCompleteView(LoginRequiredMixin, View):
    "A class to complete todo"
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Todo, id=kwargs.get('pk'))
        try:
            data = json.loads(request.body)
            task.complete = data.get("complete", False)
            task.save()
            return JsonResponse({"success": True, "completed": task.complete})
        except json.JSONDecodeError:
            return JsonResponse({"success": False}, status=400)
    


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    "A class to update todo"
    model = Todo
    form_class = TodoForm
    template_name = 'todo/todo_update.html'
    success_url = reverse_lazy('todo:todo-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.get_object()
        return context
        

class TodoDeleteView(LoginRequiredMixin, DeleteView):
    "A class to delete todo"
    model = Todo
    context_object_name = 'tasks'
    success_url = reverse_lazy('todo:todo-list')
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user.profile)