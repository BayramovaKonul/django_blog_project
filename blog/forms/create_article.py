from django import forms
from ..models import ArticleModel

class CreateArticleForm (forms.ModelForm):
    class Meta:
        model = ArticleModel
        fields = ['title', 'content', 'picture', 'published_at', 'categories', 'tags']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter the article title...',
                    'class': 'form-control mb-3',
                    'style': 'background-color: #f7f7f7; border: 1px solid #ddd;',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'placeholder': 'Write your article content here...',
                    'class': 'form-control mb-3',
                    'rows': 6,
                    'style': 'background-color: #f7f7f7; border: 1px solid #ddd;',
                }
            ),
            'picture': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control-file mb-3',
                    'style': 'background-color: #f7f7f7; border: 1px solid #ddd;',
                }
            ),
            'categories': forms.SelectMultiple(
                attrs={
                    'class': 'form-control mb-3',
                    'style': 'background-color: #f7f7f7; border: 1px solid #ddd;',
                }
            ),
            'tags': forms.SelectMultiple(
                attrs={
                    'class': 'form-control mb-3',
                    'style': 'background-color: #f7f7f7; border: 1px solid #ddd;',
                }
            ),
            'published_at' : forms.TextInput(
                            attrs = {
                                "class": "form-control mb-3",
                                "type": "datetime-local"
                                     }
            ),
        }

        
class EditArticleForm (CreateArticleForm):
    ...