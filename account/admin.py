from django.contrib import admin
from .models import CustomUserModel
from django.contrib.auth.admin import UserAdmin

@admin.register(CustomUserModel)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Profile picture Section", {"fields": ("avatar",)}),)    

