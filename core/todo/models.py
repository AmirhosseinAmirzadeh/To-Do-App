from django.db import models
from accounts.models import Profile

# Create your models here.
class Todo(models.Model):
    "A class for todo"
    user = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)
    due_time = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)