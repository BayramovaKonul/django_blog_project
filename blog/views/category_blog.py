from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models import ArticleModel, CategoryModel, CommentModel, ContactUsModel
from django.contrib import messages
from django.views import View
from account.models import CustomUserModel
from ..forms.contact_us import ContactUsForm
from django.db.models import Q, Count
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator
from blog.templatetags.custom_tags import get_categories, get_articles, get_recent_posts

def category_blog (request, category_slug):
    categories = get_categories()
    category_obj = get_object_or_404(CategoryModel, slug = category_slug)  # check the table to find asked category_slug
    category_blogs = category_obj.articles.all() # get all articles from table based on the category using related name
    blogs = get_articles()
    recent_posts = get_recent_posts
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