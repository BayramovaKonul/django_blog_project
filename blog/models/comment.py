from django.db import models
from django.contrib.auth import get_user_model
from .article import ArticleModel
from django.utils.translation import gettext as _

User = get_user_model()

class CommentModel(models.Model):
    full_name = models.CharField(max_length=100, verbose_name=("full_name"), null=False, blank=False)
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE,
                                related_name="comments", verbose_name=_("article"))
    email = models.EmailField(verbose_name=_("email"), null = True, blank=True)
    content = models.TextField(verbose_name=_("content"))
    created_at = models.DateTimeField(verbose_name=_("created_at"), auto_now_add=True)
    

    class Meta:
        db_table = 'comment'
        verbose_name = _('comment')
        verbose_name_plural = _('Comments')


    def __str__(self):
        return f"{self.article}, {self.full_name}"