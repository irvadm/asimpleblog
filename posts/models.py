from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=500)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:post_detail", kwargs={"pk": self.pk})
