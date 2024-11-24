from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models import ArticleModel, CategoryModel, CommentModel, ContactUsModel
from django.contrib import messages
from django.views import View
from account.models import CustomUserModel
from ..forms.contact_us import ContactUsForm
from django.db.models import Q, Count
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# ------------------------------------ function-based view
# @login_required(login_url='login')
# def delete_article(request, article_slug):
#     article = get_object_or_404(ArticleModel, slug = article_slug, author_id = request.user)
#     article.delete()
#     return redirect("my_articles")


# ----------------------------- delete-view
class DeleteArticleView(LoginRequiredMixin, DeleteView):
    model = ArticleModel
    template_name = 'delete_article.html'
    success_url = reverse_lazy('my_articles')