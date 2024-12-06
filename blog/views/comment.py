from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models import ArticleModel, CategoryModel, CommentModel, ContactUsModel
from django.contrib import messages
from django.views import View
from account.models import CustomUserModel
from ..forms.contact_us import ContactUsForm
from django.db.models import Q, Count
from django.views.generic import TemplateView, ListView, FormView
from django.urls import reverse
from ..forms.post_comment import CommentArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin


#---------------------------------------------------- function-based view
# @require_POST
# def post_comment(request, blog_slug):
#     details = get_object_or_404(ArticleModel, slug=blog_slug)
#     form = CommentArticleForm(request.POST)     
#     if form.is_valid():
#         comment_obj = form.save(commit=False)
#         comment_obj.user = request.user
#         comment_obj.article = details
#         comment_obj.save()
    
#     return redirect('blog/details', blog_slug=blog_slug)  # takes url name


#------------------------------------------------- form view
class CommentFormView(LoginRequiredMixin, FormView):
    form_class = CommentArticleForm
    template_name = 'blog_detail.html'

    def form_valid(self, form):
        article = get_object_or_404(ArticleModel, slug=self.kwargs['slug'])
        form.instance.user = self.request.user
        form.instance.article = article
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self): #since I need to override success_url, because it should dynamically generate the URL using slug
        return reverse('blog/details', kwargs={'slug': self.kwargs['slug']})