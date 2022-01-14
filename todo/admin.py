from django.contrib import admin
from todo.models import ToDo


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    pass
