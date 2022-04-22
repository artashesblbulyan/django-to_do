from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import Profile


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea, required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = Profile
        exclude = ['user']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
