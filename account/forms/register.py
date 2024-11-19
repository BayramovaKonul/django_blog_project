from django.contrib.auth.forms import UserCreationForm
from ..models import CustomUserModel
from django import forms

class RegisterForm (UserCreationForm):

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control mb-3",
                "type": "password"
            }
        ),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirmation",
                "class": "form-control mb-3",
                "type": "password"
            }
        ),
    )
    class Meta:
        model = CustomUserModel
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username' : forms.TextInput(
                            attrs = {
                                "placeholder": "Username",
                                "class": "form-control mb-3",
                                "type": "text"
                                     }
                                    ),
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
        }
