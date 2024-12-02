from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models import ArticleModel, CategoryModel, CommentModel, ContactUsModel
from django.contrib import messages
from django.views import View
from blog.templatetags.custom_tags import get_categories, get_recent_posts
import logging

logger = logging.getLogger("base")


def home (request):
    if request.user.is_authenticated:
        logger.info(f"Home Page is visited by id: {request.user.id}")
    else:
        logger.info(f"Home Page is visited by id: anonymous user")

    print(get_recent_posts)
    all_articles = ArticleModel.objects.all()[1:]
    categories = CategoryModel.objects.all()[:6]
    all_blogs = ArticleModel.objects.all()[:4]
    recent_posts = ArticleModel.objects.all().order_by('-created_at')[:6]
    messages.success(request, "Welcome to the website")
    return render(request, 'index.html', context={
        'all_articles':all_articles,
        'categories':categories,
        'blogs':all_blogs,
        'recent_posts':recent_posts
    })