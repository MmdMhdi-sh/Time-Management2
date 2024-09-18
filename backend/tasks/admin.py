from django.contrib import admin

from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__']
    search_fields = ['task__title']
    class Meta:
        model = Task

admin.site.register(Task, TaskAdmin)
