from django.urls import path

from .views import (
    UserProfileView
)

urlpatterns = [
    path('<str:user_username>', UserProfileView.as_view(), name='userProfile')
]