from django import template
from blog.models import ArticleModel, CategoryModel
from django.db.models import Q, Count

register = template.Library()

@register.simple_tag

def get_articles():
    return ArticleModel.objects.all()

def get_categories():
    return CategoryModel.objects.annotate(article_count=Count('articles')).order_by("-article_count").values('name', 'article_count', 'slug')

def get_recent_posts():
    return ArticleModel.objects.all().order_by('-created_at')[:4]