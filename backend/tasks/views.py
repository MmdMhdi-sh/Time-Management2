import random
from django.views import View
from django.shortcuts import redirect, render

from .forms import TaskForm
from .models import Task

def home_view(request, *args, **kwargs):
    return render()
    
class TasksListView(View):
    template_name = 'tasks/list.html'
    def get(self, request, *args, **kargs):
        # GET Method
        print('user', request.user.username)
        form = TaskForm()
        qs = Task.objects.all()
        tasks_list = [{"id": task.id, "title": task.title, "done": task.done, "duration": task.duration, "description": task.description} for task in qs]
        context = {
            'form': form,
            'response': tasks_list
        }
        return render(request, self.template_name, context)
    # def post(self, request, *args, **kargs):
    #     # POST Method
    #     form = TaskForm(request.POST or None)
    #     if form.is_valid():
    #         new_task = form.save(commit=False)
    #         new_task.duration = random.randint(1, 100)
    #         new_task.done = random.randint(0, new_task.duration)
    #         new_task.save()
    #         form = TaskForm()
    #         qs = Task.objects.all()
    #         tasks_list = [{"id": task.id, "title": task.title, "done": task.done, "duration": task.duration, "description": task.description} for task in qs]
    #     context = {
    #         'form': form,
    #         'response': tasks_list
    #     }
    #     return render(request, self.template_name, context)
tasks_list_view = TasksListView.as_view()

# def tasks_list_view(request, *args, **kwargs):
#     if request.method == 'POST':
#         form = TaskForm(request.POST or None)
#         if form.is_valid():
#             new_task = form.save(commit=False)
#             new_task.duration = random.randint(1, 100)
#             new_task.done = random.randint(0, new_task.duration)
#             new_task.save()
    # qs = Task.objects.all()
    # form = TaskForm()
    # tasks_list = [{"id": task.id, "title": task.title, "done": task.done, "duration": task.duration, "description": task.description} for task in qs]
#     context = {
#         "form": form,
#         "response": tasks_list
#     }
#     return render(request, 'tasks/list.html', context)

class TaskCreateView(View):
    template_name = 'tasks/create.html'
    def get(self, request, *args, **kargs):
        # GET Method
        form = TaskForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    def post(self, request, *args, **kargs):
        # POST Method
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.duration = random.randint(1, 100)
            new_task.done = random.randint(0, new_task.duration)
            new_task.save()
            form = TaskForm()
        context = {
            'form': form
        }
        return redirect("/tasks/list")
tasks_create_view = TaskCreateView.as_view()
# def tasks_create_view(request, *args, **kwargs): 
#     form = TaskForm(request.POST or None)
#     if form.is_valid():
#         new_task = form.save(commit=False)
#         print("new task = ", new_task)
#         new_task.done = random.randint(1, 100)
#         print("done:", new_task.done)
#         new_task.save()
#         print("new task = ", new_task)
#         form = TaskForm()
#     context = {
#         "form": form
#     }
#     return render(request, 'components/form.html', context)

class TaskUpdateView(View):
    template_name = 'tasks/update.html'
    def get(self, request, task_id, *args, **kargs):
        # GET Method
        task_obj = Task.objects.get(id=task_id)
        form = TaskForm()
        context = {
            'form': form,
            'task': task_obj
        }
        return render(request, self.template_name, context)
    def post(self, request, task_id, *args, **kargs):
        # POST Method
        task_obj = Task.objects.get(id=task_id)
        form = TaskForm(request.POST or None)
        if form.is_valid():
            if form.cleaned_data['title'] : task_obj.title = form.cleaned_data['title']
            if form.cleaned_data['description'] : task_obj.description = form.cleaned_data['description']
            if form.cleaned_data['duration'] : task_obj.duration = form.cleaned_data['duration']
            if form.cleaned_data['done'] : task_obj.done = form.cleaned_data['done']
            task_obj.save()
        return redirect("/tasks/{{ task_id }}")
tasks_update_view = TaskUpdateView.as_view()

# def tasks_update_view(request, task_id, *args, **kwargs):
    # task_obj = Task.objects.get(id=task_id)
    # if request.method == 'POST':
    #     form = TaskForm(request.POST or None)
    #     if form.is_valid():
    #         if form.cleaned_data['title'] : task_obj.title = form.cleaned_data['title']
    #         if form.cleaned_data['description'] : task_obj.description = form.cleaned_data['description']
    #         if form.cleaned_data['duration'] : task_obj.duration = form.cleaned_data['duration']
    #         if form.cleaned_data['done'] : task_obj.done = form.cleaned_data['done']
    #         task_obj.save()
    # form = TaskForm()
    # context = {
    #     "form": form,
    #     "task": task_obj
    # }
    # return render(request, 'tasks/detail.html', context)

class TasksDetailView(View):
    template_name = 'tasks/detail.html'
    def get(self, request, task_id, *args, **kwargs):
        task_obj = Task.objects.get(id=task_id)
        form = TaskForm()
        context = {
            'form': form,
            'task': task_obj
        }
        return render(request, self.template_name, context)
    
tasks_detail_view = TasksDetailView.as_view()