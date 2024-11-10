from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact_us, name = 'contact'),
    path('blogs', views.blogs, name = 'blogs'),
    path('category/<slug:category_slug>', views.category_blog, name = 'category'),
    path('blogs/<slug:blog_slug>/', views.detail_blog, name = 'blog/details'),
]
