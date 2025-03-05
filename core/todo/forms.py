from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    "A class for todo form"
    class Meta:
        model = Todo
        fields = ['title', 'due_time']