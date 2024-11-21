from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ArticleModel, CategoryModel, CommentModel, ContactUsModel
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.utils.translation import gettext as _
from .forms.contact_us import ContactUsForm
from .forms.post_comment import CommentArticleForm
from .forms.create_article import CreateArticleForm, EditArticleForm
from account.models import CustomUserModel
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from datetime import datetime
from django.utils.timezone import now
# Create your views here.


def home (request):
    messages.success(request, "Welcome to the website")
    return render(request, 'index.html')

# def about (request):
#     welcome_message = _("Welcome to my blog")
#     return render(request, 'about.html', context= {
#         'welcome_message' : welcome_message
#     })

class AboutView(TemplateView):
    template_name = 'about.html'

def contact_us (request):
    form = ContactUsForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.stage  = ContactUsModel.StageChoices.NEW
            form_obj.assigned_to = (CustomUserModel.objects.filter(is_staff=True).annotate(message_count=Count('assigned__id')).order_by('message_count').first()) # here 'assigned' is a related name
            form_obj.save()
            return redirect('home')

    return render(request, 'contact.html', context = {
        'form' : form
    })

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
    queryset = ArticleModel.objects.filter(published_at__lte=now())

    def get_queryset(self):
        queryset = super().get_queryset() 
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(Q(title__icontains=search) |
                     Q(content__icontains=search))
        return queryset
    
    def get_context_data(self, **kwargs):
        queryset = self.get_queryset()
        context = super().get_context_data(**kwargs)   #take context_object_name
        context['categories'] = CategoryModel.objects.annotate(article_count=Count('articles')).order_by("-article_count").values('name', 'article_count', 'slug')
        context['recent_posts'] = queryset.order_by('-created_at')[:4]

        return context
                 

def category_blog (request, category_slug):
    categories = CategoryModel.objects.annotate(article_count=Count('articles')).order_by("-article_count").values('name', 'article_count', 'slug')
    category_obj = get_object_or_404(CategoryModel, slug = category_slug)  # check the table to find asked category_slug
    category_blogs = category_obj.articles.all() # get all articles from table based on the category using related name
    blogs = ArticleModel.objects.all()
    recent_posts = blogs.order_by('-created_at')[:4]
    page = request.GET.get('page')
    paginator = Paginator(category_blogs, 2) 
    search = request.GET.get('search')
    if search:
        category_blogs = category_blogs.filter(Q(title__icontains=search) |
                     Q(content__icontains=search))
        
    return render(request, 'category.html', context={
        'page_obj' : paginator.get_page(page),
        'category_name' : category_obj.name,
        'recent_posts' : recent_posts,
        'categories' : categories
    })


def detail_blog (request,blog_slug):
    details = get_object_or_404(ArticleModel, slug = blog_slug)
    comments = CommentModel.objects.filter(article = details).order_by('-created_at')
    blogs = ArticleModel.objects.all()
    recent_posts = blogs.order_by('-created_at')[:4]
    categories = CategoryModel.objects.annotate(article_count=Count('articles')).order_by("-article_count").values('name', 'article_count', 'slug')
    form = CommentArticleForm()
    return render(request, 'blog_detail.html', context={
        'details' : details,
        'comments' : comments,
        'recent_posts' : recent_posts,
        'categories' : categories,
        'form' : form
    })

@require_POST
def post_comment(request, blog_slug):
    details = get_object_or_404(ArticleModel, slug=blog_slug)
    form = CommentArticleForm(request.POST)     
    if form.is_valid():
        comment_obj = form.save(commit=False)
        comment_obj.user = request.user
        comment_obj.article = details
        comment_obj.save()
    
    return redirect('blog/details', blog_slug=blog_slug)  # takes url name


# @login_required(login_url='login')
# def create_article(request):
#     form = CreateArticleForm(request.POST or None, request.FILES or None)
#     if request.method == "POST":
#         if form.is_valid():
#             article_obj = form.save(commit=False)
#             article_obj.author = request.user
#             with transaction.atomic():
#                 article_obj.save()
#                 form.save_m2m()  #to save the third table between articles and users (manytomany)
#             return redirect("home")

#     return render (request, 'create_article.html', context={
#         'form' : form
#     })

class ArticlesView(LoginRequiredMixin, View):
    http_method_names = ['get', 'post']
    form_class = CreateArticleForm

    def get(self, request):
        form = self.form_class()
        return render (request, 'create_article.html', context={
        'form' : form
        })
    # @method_decorator(login_required) - method based login_required
    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            article_obj = form.save(commit=False)
            article_obj.author = request.user
            with transaction.atomic():
                article_obj.save()
                form.save_m2m()  #to save the third table between articles and users (manytomany)
            return redirect("home")


@login_required(login_url='login')
def my_articles (request):
    page = request.GET.get('page')
    all_articles = ArticleModel.objects.filter(author_id=request.user).order_by('published_at')
    paginator = Paginator(all_articles, 3)
    current_datetime = now()

    for article in all_articles:
        article.is_unpublished = article.published_at > current_datetime

    return render (request, 'my_articles.html', context= {
        'all_articles':all_articles,
        'page_obj' : paginator.get_page(page),
        'current_datetime':current_datetime
    })

# @login_required(login_url='login')
# def edit_article(request, article_slug):
#     article = get_object_or_404(ArticleModel, slug = article_slug, author_id = request.user)
#     form = EditArticleForm(request.POST or None, request.FILES or None, instance=article)

#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect("my_articles", user_id=request.user.id)
    
#     return render(request, 'edit_article.html', context={
#         'form' : form
#     })

class EditArticle(LoginRequiredMixin, View):
    http_method_names = ['get', 'post']
    form_class=EditArticleForm

    def get_article(self):  
        article_slug = self.kwargs.get('article_slug')  #article is common for both get and post request
        article = get_object_or_404(ArticleModel, slug = article_slug, author_id = self.request.user)
        return article

    def get(self, request, article_slug):
        article = self.get_article()
        form = self.form_class(instance=article)
        return render(request, 'edit_article.html', context={
        'form' : form
    })

    def post(self, request, article_slug):
        article = self.get_article()
        form = self.form_class(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect("my_articles")



@login_required(login_url='login')
def delete_article(request, article_slug):
    article = get_object_or_404(ArticleModel, slug = article_slug, author_id = request.user)
    article.delete()
    return redirect("my_articles")