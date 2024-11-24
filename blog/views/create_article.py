from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models import ArticleModel, CategoryModel, CommentModel, ContactUsModel
from django.contrib import messages
from django.views import View
from account.models import CustomUserModel
from ..forms.contact_us import ContactUsForm
from django.db.models import Q, Count
from django.views.generic import TemplateView, ListView, FormView,CreateView
from django.urls import reverse
from ..forms.post_comment import CommentArticleForm
from django import forms
from django.urls import reverse_lazy

#--------------------------------- function-based view
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

# #--------------------------------------- class-based view
# class ArticlesView(LoginRequiredMixin, View):
#     http_method_names = ['get', 'post']
#     form_class = CreateArticleForm

#     def get(self, request):
#         form = self.form_class()
#         return render (request, 'create_article.html', context={
#         'form' : form
#         })
#     # @method_decorator(login_required) - method based login_required
#     def post(self, request):
#         form = self.form_class(request.POST, request.FILES)
#         if form.is_valid():
#             article_obj = form.save(commit=False)
#             article_obj.author = request.user
#             with transaction.atomic():
#                 article_obj.save()
#                 form.save_m2m()  #to save the third table between articles and users (manytomany)
#             return redirect("home")


#----------------------------------------- Create view
class CreateArticleView(CreateView):
    model = ArticleModel
    fields = ['title', 'content', 'picture', 'published_at', 'categories', 'tags']
    template_name = 'create_article.html'
    success_url = reverse_lazy('home')
    
    def get_form(self):  # customize the form before render
        form = super().get_form()
        form.fields['published_at'].widget = forms.DateTimeInput(attrs={
            'class': 'form-control mb-3',
            'type': 'datetime-local'
        })
        return form
    
    def form_valid(self, form): # additional logic before saving the object
        form.instance.author = self.request.user
        return super().form_valid(form)
