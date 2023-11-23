from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Contact



class LoginForm(AuthenticationForm):
    # You can customize the form if needed
    pass

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'describtion']
