import random

from django.http import Http404
from django.shortcuts import render

from .forms import TaskForm
from .models import Task

def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", {})

def tasks_list_view(request, *args, **kwargs):
    qs = Task.objects.all()
    tasks_list = [{"id": task.id, "title": task.title, "duration": task.duration, "done": task.done} for task in qs]
    data = {
        "response": tasks_list
    }
    return render(request, "tasks/list.html", data)

def tasks_create_view(request, *args, **kwargs):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task_obj = form.save(commit=False)
        task_obj.done = random.randint(0, task_obj.duration)
        task_obj.save()
        form = TaskForm()
    context = {
        "form": form
    }
    return render(request, "tasks/create.html", context)

# def tasks_delete_view(request, task_id, *args, **kwargs):
#     qs = Task.objects.filter(id=task_id)
#     if not qs.exists():
#         return Http404
#     task_obj = qs.first()
#     task_obj.detele()
#     return render() 



