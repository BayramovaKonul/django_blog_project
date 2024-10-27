from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactUsModel(models.Model):
    STAGE_CHOICES = [
    ('new', 'New'),               # Message is received but not reviewed yet, it is default value
    ('in_review', 'In Review'),   # Under review by the team or assigned person
    ('in_progress', 'In Progress'), # Actively being worked on
    ('resolved', 'Resolved'),     # Issue has been addressed
    ('closed', 'Closed')          # Final stage after verification or user confirmation
    ]


    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="messages")
    email = models.EmailField(null = False)
    subject = models.CharField(max_length=200)
    #slug = AutoSlugField(populate_from="subject", unique=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES, default='new')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank=True,
                             related_name="assigned")
    resolved_at = models.DateTimeField(null = True)
    
    class Meta:
        db_table = 'ContactUs'
        verbose_name = 'ContactUs'
        verbose_name_plural = "ContactUs"
        
    def __str__(self):
        return f"{self.user}"

