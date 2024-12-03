from django import template
from blog.models import ArticleModel, CategoryModel
from django.db.models import Q, Count
from django.utils.timezone import now

import logging

logger = logging.Logger("base")

register = template.Library()

@register.simple_tag
def get_categories():
    categories = CategoryModel.objects.annotate(article_count=Count('articles')).order_by("-article_count")
    return categories

@register.simple_tag
def get_recent_posts():
    current_datetime = now()
    recent_posts = (
    ArticleModel.objects.filter(published_at__lte=current_datetime)
    .order_by('-created_at')[:4])

    logger.info(f"Recent posts: {recent_posts}")
    return recent_posts