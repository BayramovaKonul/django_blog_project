from django.db import models
from autoslug import AutoSlugField
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .category import CategoryModel
from .tag import TagModel
from .abstract_models import CreationDateAbstractModel
from django.utils.translation import gettext as _

User = get_user_model()

class ArticleModel(CreationDateAbstractModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                                  related_name="articles", verbose_name=_("author"))
    title = models.CharField(verbose_name=_("title"), max_length=255)
    slug = AutoSlugField(populate_from="title", unique=True)
    content = models.TextField(verbose_name=_("content"))
    published_at = models.DateTimeField(verbose_name=_("published_at"), null=True, blank=True)
    picture = models.ImageField(verbose_name=_("picture"), upload_to='article_images')
    categories = models.ManyToManyField(CategoryModel, related_name="articles", verbose_name=_("categories"))
    tags = models.ManyToManyField(TagModel, related_name="articles", verbose_name=_("tags"))

    class Meta:
        db_table = 'article'
        verbose_name = _('article')
        verbose_name_plural = _("Articles")

    def __str__(self):
        return f"{self.title}, {self.author.username}"