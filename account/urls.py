from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('<int:id>/', views.user_info),   # I wrote int:id, otherwise it will take id as string, then we need to make conversion each time we need id.
    # path('<username>/', views.user_pic),
    # path('user', views.user, name = 'user'),
    path('login', views.user_login, name = 'login'),
    path('logout', views.user_logout, name = 'logout'),
    path('register', views.register, name = 'register'),
    path('change-password', views.change_password, name = 'change-password'),
    path('update-profile', views.update_profile, name = 'update-profile')
]