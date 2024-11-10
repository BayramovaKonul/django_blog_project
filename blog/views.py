from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ArticleModel, CategoryModel, CommentModel
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.utils.translation import gettext as _
# Create your views here.

def my_blogs(request):
    return HttpResponse('<h1>Welcome to my blog</h1>')

def my_blog_details(request):
    return HttpResponse('<h1>All information about my blog</h1>')

def home (request):
    return render(request, 'index.html')

def about (request):
    welcome_message = _("Welcome to my blog")
    return render(request, 'about.html', context= {
        'welcome_message' : welcome_message
    })

def contact (request):
    return render(request, 'contact.html')

def blogs (request):
    page = request.GET.get('page')  # GET - method returns dictionary from URL, get - dictionary method
    search = request.GET.get('search')
    blogs = ArticleModel.objects.all()
    categories = CategoryModel.objects.annotate(article_count=Count('articles')).order_by("-article_count").values('name', 'article_count', 'slug')
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
    
    
                 

def category_blog (request, category_slug):
    categories = CategoryModel.objects.annotate(article_count=Count('articles')).order_by("-article_count").values('name', 'article_count', 'slug')
    category_obj = get_object_or_404(CategoryModel, slug = category_slug)  # check the table to find asked category_slug
    category_blogs = category_obj.articles.all() # get all articles from table based on the category using related name
    blogs = ArticleModel.objects.all()
    recent_posts = blogs.order_by('-created_at')[:4]
    page = request.GET.get('page')
    paginator = Paginator(category_blogs, 2) 
    search = request.GET.get('search')
    if search:
        category_blogs = category_blogs.filter(Q(title__icontains=search) |
                     Q(content__icontains=search))
    return render(request, 'category.html', context={
        'page_obj' : paginator.get_page(page),
        'category_name' : category_obj.name,
        'recent_posts' : recent_posts,
        'categories' : categories
    })


def detail_blog (request,blog_slug):
    details = get_object_or_404(ArticleModel, slug = blog_slug)
    comments = CommentModel.objects.filter(article = details)
    blogs = ArticleModel.objects.all()
    recent_posts = blogs.order_by('-created_at')[:4]
    categories = CategoryModel.objects.annotate(article_count=Count('articles')).order_by("-article_count").values('name', 'article_count', 'slug')
    return render(request, 'blog_detail.html', context={
        'details' : details,
        'comments' : comments,
        'recent_posts' : recent_posts,
        'categories' : categories
    })