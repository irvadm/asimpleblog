from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    list_display = ['pk', 'content', 'creator']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'creator', 'body']
    list_display_links = ['pk']
    list_editable = ['title', 'body']
    inlines = [CommentInline]
