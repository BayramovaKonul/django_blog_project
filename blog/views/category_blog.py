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
from blog.templatetags.custom_tags import get_categories, get_recent_posts
import logging

logger = logging.getLogger("base")

def category_blog (request, category_slug):
    category_obj = get_object_or_404(CategoryModel, slug = category_slug)  # check the table to find asked category_slug
    category_blogs = category_obj.articles.all() # get all articles from table based on the category using related name
    recent_posts = get_recent_posts
    page = request.GET.get('page') 
    search = request.GET.get('search')
    if search:
        category_blogs = category_blogs.filter(Q(title__icontains=search) |
                     Q(content__icontains=search))
        if category_blogs:
            logger.info(f"{request.user} searched for {search} and results have been shown")
        else:
            logger.info(f"{search} can not be found")

    paginator = Paginator(category_blogs, 2)
   
    return render(request, 'category.html', context={
        'page_obj' : paginator.get_page(page),
        'category_name' : category_obj.name,
        'recent_posts' : recent_posts,
    })

class AllArticlesView(ListView):
    model = ArticleModel
    template_name = 'blog.html'
    context_object_name = 'articles'
    paginate_by = 2
    page_kwarg = 'page'

    def get_queryset(self):
        queryset = super().get_queryset() 
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(Q(title__icontains=search) |
                     Q(content__icontains=search))
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   #take context_object_name
        context['categories'] = get_categories()
        context['recent_posts'] = get_recent_posts()

        return context