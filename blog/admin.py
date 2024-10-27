from django.contrib import admin

# Register your models here.
from .models import CategoryModel, ArticleModel

admin.site.register(CategoryModel)
@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'published_at'] # which fields should be shown
    list_display_links = ['title', 'created_at'] # make each field a link
    search_fields = ['title', 'content'] # search can be done by title and content
    list_filter = ['created_at']