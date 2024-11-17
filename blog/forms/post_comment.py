from django import forms
from ..models import CommentModel

class CommentArticleForm (forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['content']
        widgets = {
            'content' : forms.Textarea(
                            attrs = {
                                "placeholder": "Comment Area",
                                "class": "form-control mb-3",
                                "row" : "3",
                                "id" : "exampleFormControlTextarea1"
                                     }
                                    )
        }
