from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class JoinForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'newpassword'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'size': '30'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        help_texts = {
         'username': None
 }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())