from django import forms
from django.contrib.auth.models import User
from django.core.files import File

from PIL import Image

from .models import Profile


class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), max_length=50, required=False)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), max_length=50, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', ]


class ProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}), max_length=300, required=False)
    facebook_account = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), max_length=200, required=False)
    twitter_account = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), max_length=200, required=False)

    class Meta:
        model = Profile
        fields = ['bio', 'facebook_account', 'twitter_account']


class PictureForm(forms.ModelForm):
    picture = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={'class': 'form-control-file'}), required=False)

    class Meta:
        model = Profile
        fields = ['picture']
