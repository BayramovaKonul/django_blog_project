from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    # path('about', views.about, name = 'about'),
    path('about', views.AboutView.as_view(), name = 'about'),
    path('contact', views.contact_us, name = 'contact'),
    # path('blogs', views.blogs, name = 'blogs'),
    path('blogs', views.AllArticlesView.as_view(), name = 'blogs'),
    path('category/<slug:category_slug>', views.category_blog, name = 'category'),
    path('blogs/<slug:blog_slug>/', views.detail_blog, name = 'blog/details'),
    # path('create-article', views.create_article, name = 'create-article'),
    path('create-article', views.ArticlesView.as_view(), name = 'create-article'),
    path('my-articles', views.my_articles, name = 'my_articles'),
    # path('edit-article/<slug:article_slug>/', views.edit_article, name = 'edit-article'),
    path('edit-article/<slug:article_slug>/', views.EditArticle.as_view(), name = 'edit-article'),
    path('delete-article/<slug:article_slug>/', views.delete_article, name = 'delete-article'),
    path('post-comment/<slug:blog_slug>/', views.post_comment, name = 'post-comment'),
]
