from django import forms
from ..models import CustomUserModel

class LoginForm (forms.Form): 
        username = forms.CharField(
                max_length=100,
                widget=forms.TextInput(attrs={
                    'placeholder': 'Username',
                    'class': 'form-control mb-3',
                    'type': 'text',
                    'name': 'username'
        })
        )
        password = forms.CharField(
                widget= forms.PasswordInput(attrs={
                    'placeholder': 'Password',
                    'class': 'form-control mb-3',
                    'type': 'password',
                    'name': 'password1'
        })
        )
        