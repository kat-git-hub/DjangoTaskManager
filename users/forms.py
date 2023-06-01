from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from users.models import User
from django.utils.translation import gettext as _


class UserForm(UserCreationForm):
    first_name = forms.CharField(label=_('first_name'))
    last_name = forms.CharField(label=_('last_name'))
    password1 = forms.CharField(label=_('Password'))
    password2 = forms.CharField(label=_('Password confirmation'))
    

    class Meta():
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')


class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.username[_('username')]
            password = self.cleaned_data[_('Password')]
            if not authenticate(user=username, password=password):
                raise forms.ValidationError("Invalid login")
