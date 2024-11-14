from django import forms
from ..models import ContactUsModel
class ContactUsForm (forms.ModelForm):
    class Meta:
        model = ContactUsModel
        fields = ['email', 'subject', 'message']
        widgets = {
            'email' : forms.TextInput(
                            attrs = {
                                "placeholder": "email",
                                "class": "form-control mb-3",
                                "type": "email"
                                     }
                                    ),
            'subject' : forms.TextInput(
                            attrs = {
                                "placeholder": "subject",
                                "class": "form-control mb-3",
                                    }
                                    ),
            'message' : forms.Textarea(
                            attrs = {
                                "placeholder": "message",
                                "class": "form-control mb-3",
                                "row" : "5"
                                     }
                                    )
        }


    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < 5:
            raise forms.ValidationError("Message must be gretaer than 5")
        
        return message