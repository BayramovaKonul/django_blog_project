from django.contrib import admin

# Register your models here.
from .models import CategoryModel, ArticleModel, CommentModel

admin.site.register(CategoryModel)
@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'published_at'] # which fields should be shown
    list_display_links = ['title', 'created_at'] # make each field a link
    search_fields = ['title', 'content'] # search can be done by title and content
    list_filter = ['created_at']



@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'article', 'user', 'created_at'] # which fields should be shown
    list_display_links = ['user', 'article'] # make each field a link
    search_fields = ['user', 'article'] # search can be done by title and content
    list_filter = ['created_at']

