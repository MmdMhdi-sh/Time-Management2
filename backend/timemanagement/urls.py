"""
URL configuration for timemanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from two_factor.urls import urlpatterns as tf_urls

from tasks.views import tasks_list_view

urlpatterns = [
    path('', tasks_list_view, name='homePage'),
    path(r'', include(tf_urls)),
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('profile/', include('profiles.urls')),
    path('tasks/', include('tasks.urls')),
    path('api/', include('api.urls'))
]
