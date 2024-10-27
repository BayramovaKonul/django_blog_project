from django.db import models
from django.contrib.auth import get_user_model
from .article import ArticleModel

User = get_user_model()

class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="comments")
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE,
                                related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comment'
        verbose_name = 'comment'
        verbose_name_plural = 'Comments'