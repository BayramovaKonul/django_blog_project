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
from ..forms.post_comment import CommentArticleForm
from blog.templatetags.custom_tags import get_categories, get_recent_posts

def detail_blog (request,slug):
    details = get_object_or_404(ArticleModel, slug = slug)
    print (details.slug)
    comments = CommentModel.objects.filter(article = details).order_by('-created_at')
    recent_posts = get_recent_posts()
    form = CommentArticleForm()
    categories = get_categories()
    return render(request, 'blog_detail.html', context={
        'details':details,
        'comments' : comments,
        'recent_posts' : recent_posts,
        'categories' : categories,
        'form':form
    })