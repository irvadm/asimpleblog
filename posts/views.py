from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import PostForm
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            messages.success(request, 'New post successfully created!')
            return redirect(new_post.get_absolute_url())
    form = PostForm()
    return render(request, 'posts/post_create.html', {'form': form})


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post successfully edited!')
            return redirect(post.get_absolute_url())
    else:
        form = PostForm(instance=post)
        return render(request, 'posts/post_update.html', {'form': form, 'post': post})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post successfully deleted!')
        return redirect(reverse('posts:post_list'))
    else:
        return render(request, 'posts/post_delete.html', {'post': post})
