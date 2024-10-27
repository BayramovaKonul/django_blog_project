from django.contrib import admin

# Register your models here.
from .models import CategoryModel, ArticleModel


admin.site.register(CategoryModel)
