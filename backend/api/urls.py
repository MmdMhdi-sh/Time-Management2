from django.contrib import admin
from django.urls import path, include

from .views import (
    task_list_view,
)

urlpatterns = [
    path('tasks', task_list_view),
]