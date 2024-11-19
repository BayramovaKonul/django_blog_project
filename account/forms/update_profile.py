from django.contrib.auth.forms import UserChangeForm
from ..models import CustomUserModel
from django import forms

class UpdateProfileForm(UserChangeForm):
    class Meta:
        model = CustomUserModel
        fields = ['email', 'first_name', 'last_name', 'avatar']
        widgets = {
            'email' : forms.EmailInput(
                            attrs = {
                                "placeholder": "Email",
                                "class": "form-control mb-3",
                                "type" : "email"
                                    }
                                    ),
            'first_name' : forms.TextInput(
                            attrs = {
                                "placeholder": "First Name",
                                "class": "form-control mb-3",
                                "type": "text"
                                     }
                                    ),
            'last_name' : forms.TextInput(
                            attrs = {
                                "placeholder": "Last Name",
                                "class": "form-control mb-3",
                                "type": "text"
                                     }
                                    ),
            'avatar': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control-file mb-3',
                    'style': 'background-color: #f7f7f7; border: 1px solid #ddd;',
                }
            ),
        }
