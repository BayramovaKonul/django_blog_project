from django.db import models
from autoslug import AutoSlugField
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .category import CategoryModel
#from .abtract_models import CreationDateAbstractModel
User = get_user_model()

class ArticleModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                                  related_name="articles")
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from="title", unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # take the currect time
    modified_at = models.DateTimeField(auto_now=True) # each time the modified time write to the database
    published_at = models.DateTimeField(null=True, blank=True)
    picture = models.ImageField(upload_to='article_images')
    categories = models.ManyToManyField(CategoryModel)

    class Meta:
        db_table = 'article'
        verbose_name = 'article'
        verbose_name_plural = "Articles"

    def __str__(self):
        return f"{self.title}, {self.author.username}"