from django import forms

class ContactForm(forms.Form):
    
    subject = forms.CharField(max_length=50, label="Subject", required=True)
    email = forms.EmailField(label="Email", required=True)
    message = forms.CharField(widget=forms.Textarea, label="Message", required=True)
    
