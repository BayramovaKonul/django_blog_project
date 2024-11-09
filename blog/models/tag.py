from django.db import models
from autoslug import AutoSlugField

class TagModel(models.Model):
    name = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from="name", unique=True)
    created_at = models.DateTimeField(null = True, blank = True)

    class Meta:
        db_table = 'tag'
        verbose_name = 'Tag'
        verbose_name_plural = "Tags"

    def __str__(self):
        return f"{self.name}"