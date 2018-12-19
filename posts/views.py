from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import PostForm, CommentForm
from .models import Post, Comment


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            new_post.creator = request.user
            new_post.save()
            messages.add_message(request, messages.SUCCESS,
                                 'New post successfully created!')
            return redirect(new_post.get_absolute_url())
    form = PostForm()
    return render(request, 'posts/post_create.html', {'form': form})


@login_required
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


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post successfully deleted!')
        return redirect(reverse('posts:post_list'))
    else:
        return render(request, 'posts/post_delete.html', {'post': post})


@login_required
def comment_create(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save()
            new_comment.creator = request.user
            new_comment.post = post
            new_comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment created!')
            return redirect(post.get_absolute_url())
        else:
            messages.add_message(request, messages.ERROR,
                                 'Problem creating comment.')
            return render(request, 'posts/comment_create.html', {'form': form})
    else:
        form = CommentForm()
        return render(request, 'posts/comment_create.html', {'form': form, 'post': post})


@login_required
def comment_update(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(data=request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment saved.')
            return redirect(comment.post.get_absolute_url())
    else:
        form = CommentForm(instance=comment)
        return render(request, 'posts/comment_update.html', {'form': form, 'comment': comment})


@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Comment deleted.')
        return redirect(reverse('posts:post_list'))
    else:
        return render(request, 'posts/comment_delete.html', {'comment': comment})
