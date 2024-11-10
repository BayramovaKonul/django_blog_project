from django import forms

class ContactUsForm (forms.Form):
    email = forms.EmailField(max_length=100, min_length=5, initial="@gmail.com", widget=forms.TextInput(
        attrs = {
            "placeholder": "email",
            "class": "form-control mb-3",
            "type": "email"
        }
    ))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs = {
            "placeholder": "subject",
            "class": "form-control mb-3",
        }
    ))
    message = forms.CharField(widget=forms.Textarea(
        attrs = {
            "placeholder": "message",
            "class": "form-control mb-3",
            "row" : "5"
        }
    ))

    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < 5:
            raise forms.ValidationError("Message must be gretaer than 5")
        
        return message