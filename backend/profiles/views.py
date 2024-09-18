from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render

from .models import Profile
from tasks.models import Task
from tasks.forms import TaskForm
User = settings.AUTH_USER_MODEL

class UserProfileView(View, LoginRequiredMixin):
    template_name = 'profiles/profile.html'
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        user = request.user
        qs = Task.objects.filter(user=user)
        tasks_list = [{"id": task.id, "title": task.title, "done": task.done, "duration": task.duration, "description": task.description} for task in qs]
        context = {
            'form': form,
            'user': user,
            'response': tasks_list
        }
        return render(request, self.template_name, context)