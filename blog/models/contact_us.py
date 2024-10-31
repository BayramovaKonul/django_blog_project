from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from .abstract_models import CreationDateAbstractModel

User = get_user_model()

class ContactUsModel(CreationDateAbstractModel):
    class StageChoices(models.TextChoices):
        NEW = 'new', 'New'
        IN_REVIEW = 'in_review', 'In Review'
        IN_PROGRESS = 'in_progress', 'In Progress'
        RESOLVED = 'resolved', 'Resolved'
        CLOSED = 'closed', 'Closed'


    email = models.EmailField(null = False)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    stage = models.CharField(max_length=20, choices=StageChoices.choices, default=StageChoices.NEW)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank=True,
                             related_name="assigned")
    resolved_at = models.DateTimeField(null = True, blank = True)
    
    class Meta:
        db_table = 'user_messages'
        verbose_name = 'ContactUs'
        verbose_name_plural = "ContactUs"
        
    def __str__(self):
        return f"{self.subject}"

