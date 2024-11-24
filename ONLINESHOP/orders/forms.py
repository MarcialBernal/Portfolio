from django import forms

class ContactForm(forms.Form):
    
    about = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()