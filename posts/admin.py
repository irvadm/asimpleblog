from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'creator', 'body']
    list_display_links = ['pk']
    list_editable = ['title', 'body']
    inlines = [CommentInline]
