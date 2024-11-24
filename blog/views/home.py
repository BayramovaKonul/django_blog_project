from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models import ArticleModel, CategoryModel, CommentModel, ContactUsModel
from django.contrib import messages
from django.views import View
from blog.templatetags.custom_tags import get_categories, get_articles, get_recent_posts


def home (request):
    all_articles = get_articles()
    recent_posts = get_recent_posts()
    categories = CategoryModel.objects.all()[:6]
    all_blogs = ArticleModel.objects.all()[:4]
    messages.success(request, "Welcome to the website")
    return render(request, 'index.html', context={
        'all_articles':all_articles,
        'recent_posts':recent_posts,
        'categories':categories,
        'blogs':all_blogs
    })