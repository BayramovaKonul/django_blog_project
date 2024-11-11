from django.db import models
from autoslug import AutoSlugField
from django.utils.translation import gettext as _

class TagModel(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=150)
    slug = AutoSlugField(populate_from="name", unique=True)
    created_at = models.DateTimeField(verbose_name=_("created_at"), null = True, blank = True)

    class Meta:
        db_table = 'tag'
        verbose_name = _('Tag')
        verbose_name_plural = _("Tags")

    def __str__(self):
        return f"{self.name}"