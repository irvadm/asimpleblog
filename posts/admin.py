from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'creator', 'body']
    list_display_links = ['title']
    list_editable = ['body']
    inlines = [CommentInline]
