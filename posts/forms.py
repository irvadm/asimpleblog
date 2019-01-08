from django import forms

from markdown_deux.templatetags.markdown_deux_tags import markdown_allowed
from pagedown.widgets import PagedownWidget

from .models import Post, Comment


class PostForm(forms.ModelForm):
    title = forms.CharField()
    body = forms.CharField(
        widget=PagedownWidget(),
        help_text=markdown_allowed()
    )

    class Meta:
        model = Post
        fields = ['title', 'body']
