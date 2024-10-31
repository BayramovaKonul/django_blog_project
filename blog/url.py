from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('all', views.my_blogs),
    path('detail', views.my_blog_details)
]
