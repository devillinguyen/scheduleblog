"""
Definition of forms.
"""

from django import forms
import re
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class RegistationForm(forms.Form):
    username =forms.CharField(max_length=254, widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    email = forms.CharField(widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
    passwordconfirm = forms.CharField(widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
    # 
    def clean_passwordconfirm(seft):
        if 'password' in seft.cleaned_data:
           password = seft.cleaned_data['password']
           passwordconfirm = seft.cleaned_data['passwordconfirm']
           if(password == passwordconfirm):
               return passwordconfirm
           raise forms.ValidationError("Mat khau khong hop le")
    #
    def clean_username(seft):
           username =seft.cleaned_data['username']
           if not re.search(r'^\w+$',username):
               raise forms.ValidationError("Tai khoan co ki tu dac biet")
           try:
               User.objects.get(username = username)
           except ObjectDoesNotExist:
               return username
           raise forms.ValidationError("Tai khoan da ton tai")
                