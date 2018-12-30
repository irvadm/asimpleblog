from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.URLField(blank=True)
    body = models.TextField(max_length=4000)
    creator = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:post_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    content = models.TextField(max_length=400)
    creator = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return '{} - {}'.format(self.content, self.creator.username)
