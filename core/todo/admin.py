from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    "A class for todo admin page"
    list_display = ('user', 'title', 'complete', 'due_time', 'created_date', 'updated_date')

    
admin.site.register(Todo, TodoAdmin)