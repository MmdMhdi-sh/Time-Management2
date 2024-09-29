from django.urls import include, path

from two_factor.urls import urlpatterns as tf_urls

from .views import (
    UserLoginView,
    UserLogoutView,
    UserRegisterView
)


urlpatterns = [
    path('login', UserLoginView.as_view(), name='userLogin'),
    path('logout', UserLogoutView.as_view(), name='userLogout'),
    path('register', UserRegisterView.as_view(), name='userRegister')
]