from django import forms
from ..models import CommentModel

class CommentArticleForm (forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['full_name', 'email', 'content']
        widgets = {
            'full_name' : forms.TextInput(
                            attrs = {
                                "placeholder": "Full Name",
                                "class": "form-control",
                                "type": "text",
                                "aria-label":"Full name"
                                     }
                                    ),
            'email' : forms.EmailInput(
                            attrs = {
                                "placeholder": "Email adress",
                                "class": "form-control",
                                "type": "email",
                                "aria-label":"Email adress"
                                    }
                                    ),
            'content' : forms.Textarea(
                            attrs = {
                                "placeholder": "Comment area",
                                "class": "form-control",
                                "rows" : "3",
                                "id" : "exampleFormControlTextarea1"
                                     }
                                    )
        }


