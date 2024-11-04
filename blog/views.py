from django.shortcuts import render
from django.http import HttpResponse
from .models import ArticleModel, CategoryModel
from django.core.paginator import Paginator
from django.db.models import Q, Count
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
    page = request.GET.get('page')  # GET - method returns dictionary from URL, get - dictionary method
    search = request.GET.get('search')
    blogs = ArticleModel.objects.all()
    categories = CategoryModel.objects.annotate(article_count=Count('articles')).values('slug', 'article_count')
    recent_posts = blogs.order_by('-created_at')[:4]
    if search:
        blogs = blogs.filter(Q(title__icontains=search) |
                     Q(content__icontains=search))
    paginator = Paginator(blogs, 2)
    return render(request, 'blog.html', 
                  context={"page_obj" : paginator.get_page(page),
                           "recent_posts": recent_posts,
                           "categories" : categories
                           })
    
    
                 

def category (request):
    return render(request, 'category.html')

def detail (request,id):
    return render(request, 'detail.html')