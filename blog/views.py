from django.shortcuts import render, get_object_or_404
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
    categories = get_object_or_404(CategoryModel, slug = category_slug)  # check the table to find asked category_slug
    category_blogs = categories.articles.all() # get all articles from table based on the category using related name
    return render(request, 'category.html', context={
        'category_blogs' : category_blogs,
        'category_name' : categories.name
    })

def detail (request,id):
    return render(request, 'detail.html')