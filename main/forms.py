from django import forms
from django.forms import TextInput, Textarea, ModelForm

from .models import HelpRequest


class UserLoginForm(forms.Form):
    # username = forms.CharField(max_length=100)
    username = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.Form):
    userlogin = forms.CharField(widget=forms.Field)

    username = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.CharField(widget=forms.EmailInput)

    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)


class HelpRequestForm(ModelForm):
    class Meta:
        model = HelpRequest
        fields = ['support_type', 'contain_of_help', 'beneficiary']

