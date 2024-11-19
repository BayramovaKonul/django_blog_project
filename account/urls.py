from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('login', views.user_login, name = 'login'),
    path('login', views.LoginView.as_view(), name = 'login'),
    path('logout', views.user_logout, name = 'logout'),
    path('register', views.register, name = 'register'),
    path('change-password', views.change_password, name = 'change-password'),
    path('update-profile', views.update_profile, name = 'update-profile')
]