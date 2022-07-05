from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    #password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput())
    #password2 = forms.CharField(label=_('Repeat Password'), widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')