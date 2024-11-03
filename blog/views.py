from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_blogs(request):
    return HttpResponse('<h1>Welcome to my blog</h1>')

def my_blog_details(request):
    return HttpResponse('<h1>All information about my blog</h1>')

def home (request):
    return render(request, 'index.html')

def about (request):
    return render(request, 'about.html')

def contact (request):
    return render(request, 'contact.html')

def blogs (request):
    return render(request, 'blog.html')

def category (request):
    return render(request, 'category.html')

def detail (request,id):
    return render(request, 'detail.html')