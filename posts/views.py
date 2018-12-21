from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, Page, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404

from .forms import PostForm
from .models import Post, Comment

import logging

logger = logging.getLogger(__name__)

# ===== Post views =====


def post_list(request):
    post_qs = Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(post_qs, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
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
            messages.add_message(request, messages.SUCCESS, 'Post created.')
            return redirect(new_post.get_absolute_url())
    form = PostForm()
    return render(request, 'posts/post_create.html', {'form': form})


@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.creator != request.user:
        return render(request, '403.html', {'message': "You cannot edit another user's post."}, status=403)
    if request.method == 'POST':
        form = PostForm(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Post saved.')
            return redirect(post.get_absolute_url())
    else:
        form = PostForm(instance=post)
        return render(request, 'posts/post_update.html', {'form': form, 'post': post})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Post deleted.')
        return redirect(reverse('posts:post_list'))
    else:
        return render(request, 'posts/post_delete.html', {'post': post})


def post_search(request):
    query = request.GET.get('query')
    posts = get_list_or_404(
        Post, Q(title__icontains=query) | Q(body__icontains=query))
    return render(request, 'posts/post_search.html', {'posts': posts, 'query': query})


# ===== Comment views =====
@login_required
def comment_create(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        new_comment = Comment.objects.create(
            content=content,
            creator=request.user,
            post=post
        )
        messages.add_message(request, messages.SUCCESS, 'Comment created.')
        return redirect(post.get_absolute_url())
    else:
        return redirect(post.get_absolute_url())


@login_required
def comment_update(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.creator != request.user:
        return render(request, '403.html', {'message': "You cannot edit another user's comment."}, status=403)
    if request.method == 'POST':
        content = request.POST.get('content')
        logger.info('New comment: {}'.format(content))
        comment.content = content
        comment.save()
        messages.add_message(request, messages.SUCCESS, 'Comment saved.')
        return redirect(comment.post.get_absolute_url())
    else:
        return render(request, 'posts/comment_update.html', {'comment': comment})


@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted.')
        return redirect(reverse('posts:post_list'))
    else:
        return render(request, 'posts/comment_delete.html', {'comment': comment})
