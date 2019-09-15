from django.conf import settings as django_settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from PIL import Image

import os


def update_filename(instance, filename):
    path = "profile_image/"
    ext = filename.split('.')[-1]
    dir_path = os.path.join(django_settings.MEDIA_ROOT, path)
    # for f in os.listdir(dir_path):

    fmt = '{}.{}'.format(instance.user.username, 'png')
    return os.path.join(path, fmt)


class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
    picture = models.ImageField(
        upload_to=update_filename, blank=True,  null=True)
    bio = models.TextField(max_length=300, blank=True)
    facebook_account = models.URLField(
        'Facebook profile', max_length=200, blank=True)
    twitter_account = models.URLField(
        'Twitter profile', max_length=200, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
