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
from django.contrib.auth.decorators import login_required
import logging
from django.utils.timezone import now


logger = logging.getLogger("base")


@login_required(login_url='login')
def my_articles (request):
    page = request.GET.get('page')
    current_datetime = now()
    filter_choice = request.GET.get('filter') 

    all_articles = ArticleModel.objects.filter(author_id=request.user.id).order_by('published_at')

    if filter_choice == 'published':
        filtered_articles = all_articles.filter(published_at__lte=current_datetime)
    elif filter_choice == 'unpublished':
        filtered_articles = all_articles.filter(published_at__gt=current_datetime) 
    else:
        filtered_articles = all_articles
        
    paginator = Paginator(filtered_articles, 3)

    return render (request, 'my_articles.html', context= {
        'page_obj' : paginator.get_page(page),
        'current_datetime':current_datetime,
    })
