from django.shortcuts import reverse
from django.test import Client, TestCase

from posts.models import Post
from posts.views import post_create, post_update, post_delete
import logging

logger = logging.getLogger(__name__)


class PostViewTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title='post 1', body='body of post 1')

    def test_success_status_code_for_existing_post(self):
        resp = self.client.get(
            reverse('posts:post_detail', kwargs={'pk': self.post.pk})
        )
        self.assertEqual(resp.status_code, 200)

    def test_404_status_code_for_non_existing_post(self):
        resp = self.client.get(
            reverse('posts:post_detail', kwargs={'pk': 2})
        )
        self.assertEqual(resp.status_code, 404)


class PostCreateViewTests(TestCase):
    def setUp(self):
        self.url = reverse('posts:post_create')

    def test_get_success_url(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)

    def test_post_success_
