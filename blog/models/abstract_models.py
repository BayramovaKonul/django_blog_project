from django.db import models

class CreationDateAbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # take the currect time
    modified_at = models.DateTimeField(auto_now=True) # each time the modified time write to the database

    class Meta:
        abstract = True