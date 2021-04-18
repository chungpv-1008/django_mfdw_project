from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your name")
    email = forms.EmailField(required=True, label="Your email")
    subject = forms.CharField(max_length=80)
    message = forms.CharField(widget=forms.Textarea)
