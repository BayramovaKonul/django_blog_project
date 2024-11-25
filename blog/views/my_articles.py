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

logger = logging.getLogger("base")


@login_required(login_url='login')
def my_articles (request):
    page = request.GET.get('page')
    logger.debug(f"Pagination page = {page}")
    all_articles = ArticleModel.objects.filter(author_id = request.user)
    paginator = Paginator(all_articles, 3) 
    return render (request, 'my_articles.html', context= {
        'all_articles':all_articles,
        'page_obj' : paginator.get_page(page),
    })