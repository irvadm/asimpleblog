# Generated by Django 2.1.4 on 2019-01-14 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to=users.models.update_filename)),
                ('bio', models.TextField(blank=True, max_length=300)),
                ('facebook_account', models.URLField(blank=True, verbose_name='Facebook profile')),
                ('twitter_account', models.URLField(blank=True, verbose_name='Twitter profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
