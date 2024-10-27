from django.db import models
from autoslug import AutoSlugField

class CategoryModel(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    slug = AutoSlugField(populate_from="name", unique=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return f"{self.name} --> {self.slug}"