from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

from .forms import PostForm
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
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
    post = Post.objects.get(pk=pk)
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
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post successfully deleted!')
        return redirect(reverse('posts:post_list'))
    else:
        return render(request, 'posts/post_delete.html', {'post': post})
