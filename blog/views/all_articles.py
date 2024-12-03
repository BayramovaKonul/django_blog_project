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
from blog.templatetags.custom_tags import get_categories, get_recent_posts
from django.utils.timezone import now

# def blogs (request):
#     page = request.GET.get('page')  # GET - method returns dictionary from URL, get - dictionary method
#     search = request.GET.get('search')
#     blogs = ArticleModel.objects.all()
#     categories = CategoryModel.objects.annotate(article_count=Count('articles')).order_by("-article_count").values('name', 'article_count', 'slug')
#     recent_posts = blogs.order_by('-created_at')[:4]
#     if search:
#         blogs = blogs.filter(Q(title__icontains=search) |
#                      Q(content__icontains=search))
#     paginator = Paginator(blogs, 2)
#     return render(request, 'blog.html', 
#                   context={"page_obj" : paginator.get_page(page),
#                            "recent_posts": recent_posts,
#                            "categories" : categories
#                            })

class AllArticlesView(ListView):
    model = ArticleModel
    template_name = 'blog.html'
    context_object_name = 'articles'
    paginate_by = 2
    page_kwarg = 'page'

    def get_queryset(self):
        current_datetime = now()
        queryset = super().get_queryset()
        queryset = queryset.filter(published_at__lte=current_datetime)
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