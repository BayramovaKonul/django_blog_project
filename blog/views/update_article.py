from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models import ArticleModel, CategoryModel, CommentModel, ContactUsModel
from django.contrib import messages
from django.views import View
from account.models import CustomUserModel
from ..forms.contact_us import ContactUsForm
from django.db.models import Q, Count
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

#----------------------------------- function-based view
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

#--------------------------------- class-based view
# class EditArticle(LoginRequiredMixin, View):
#     http_method_names = ['get', 'post']
#     form_class=EditArticleForm

#     def get_article(self):  
#         article_slug = self.kwargs.get('article_slug')  #article is common for both get and post request
#         article = get_object_or_404(ArticleModel, slug = article_slug, author_id = self.request.user)
#         return article

#     def get(self, request, article_slug):
#         article = self.get_article()
#         form = self.form_class(instance=article)
#         return render(request, 'edit_article.html', context={
#         'form' : form
#     })

#     def post(self, request, article_slug):
#         article = self.get_article()
#         form = self.form_class(request.POST, request.FILES, instance=article)
#         if form.is_valid():
#             form.save()
#             return redirect("my_articles")
        
#------------------------------------ Update-view
class UpdateArticleView(LoginRequiredMixin, UpdateView):
    model = ArticleModel
    template_name = 'edit_article.html'
    success_url = reverse_lazy('my_articles')
    fields = ['title', 'content', 'picture', 'published_at', 'categories', 'tags']