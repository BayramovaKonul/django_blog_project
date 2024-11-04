from django.db import models
from autoslug import AutoSlugField
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .category import CategoryModel
from .abstract_models import CreationDateAbstractModel

User = get_user_model()

class ArticleModel(CreationDateAbstractModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                                  related_name="articles")
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from="title", unique=True)
    content = models.TextField()
    published_at = models.DateTimeField(null=True, blank=True)
    picture = models.ImageField(upload_to='article_images')
    categories = models.ManyToManyField(CategoryModel, related_name="articles")

    class Meta:
        db_table = 'article'
        verbose_name = 'article'
        verbose_name_plural = "Articles"

    def __str__(self):
        return f"{self.title}, {self.author.username}"