import random
from django.shortcuts import render

from .forms import TaskForm
from .models import Task

def home_view(request, *args, **kwargs):
    return render()
    

def tasks_list_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.duration = random.randint(1, 100)
            new_task.done = random.randint(0, new_task.duration)
            new_task.save()
    qs = Task.objects.all()
    form = TaskForm()
    tasks_list = [{"id": task.id, "title": task.title, "done": task.done, "duration": task.duration, "description": task.description} for task in qs]
    context = {
        "form": form,
        "response": tasks_list
    }
    return render(request, 'tasks/list.html', context)
    
def tasks_create_view(request, *args, **kwargs): 
    form = TaskForm(request.POST or None)
    if form.is_valid():
        new_task = form.save(commit=False)
        print("new task = ", new_task)
        new_task.done = random.randint(1, 100)
        print("done:", new_task.done)
        new_task.save()
        print("new task = ", new_task)
        form = TaskForm()
    context = {
        "form": form
    }
    return render(request, 'components/form.html', context)

def tasks_update_view(request, task_id, *args, **kwargs):
    task_obj = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            if form.cleaned_data['title'] : task_obj.title = form.cleaned_data['title']
            if form.cleaned_data['description'] : task_obj.description = form.cleaned_data['description']
            if form.cleaned_data['duration'] : task_obj.duration = form.cleaned_data['duration']
            if form.cleaned_data['done'] : task_obj.done = form.cleaned_data['done']
            task_obj.save()
    form = TaskForm()
    context = {
        "form": form,
        "task": task_obj
    }
    return render(request, 'tasks/detail.html', context)
