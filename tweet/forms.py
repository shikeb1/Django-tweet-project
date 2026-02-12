from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    captcha=CaptchaField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'captcha')
