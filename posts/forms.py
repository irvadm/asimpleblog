from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '5', 'autofocus': True}))

    class Meta:
        model = Comment
        fields = ['content']
