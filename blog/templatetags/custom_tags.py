from django import template
from blog.models import ArticleModel, CategoryModel
from django.db.models import Q, Count

register = template.Library()

@register.simple_tag
def get_categories():
    categories = CategoryModel.objects.annotate(article_count=Count('articles')).order_by("-article_count")
    for category in categories:
        print(f"Category: {category.name}, Article count: {category.article_count}, Slug: {category.slug}")
    return categories


def get_recent_posts():
    return ArticleModel.objects.all().order_by('-created_at')[:4]