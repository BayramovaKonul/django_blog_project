from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUserModel(AbstractUser):
    avatar = models.ImageField(upload_to='user_profile_pictures/', blank = True, null= True)

    class Meta:
        db_table = 'user'
        verbose_name  = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return "{} --> {}".format(self.username, self.email)    