from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('<int:id>/', views.user_info),   # I wrote int:id, otherwise it will take id as string, then we need to make conversion each time we need id.
    # path('<username>/', views.user_pic),
    path('user', views.user, name = 'user'),
    path('login', views.login, name = 'login'),
    path('register', views.register, name = 'register'),
]