from django.contrib import admin
from .models import ToDo
# Register your models here.

class ToDoAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'start_time', 'end_time', 'todo_type')
admin.site.register(ToDo, ToDoAdmin)