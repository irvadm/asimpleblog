from django.contrib import admin
from django.db import models

from pagedown.widgets import AdminPagedownWidget

from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    list_display = ['pk', 'content', 'creator']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
    list_display = ['title', 'creator', 'body', 'pk']
    inlines = [CommentInline]
