from django import forms
from .models import User_model


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    Confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User_model
        fields = ('email','Name', 'password','Confirm')


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User_model
        fields = ('email', 'password')







