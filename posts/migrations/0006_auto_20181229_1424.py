# Generated by Django 2.1.4 on 2018-12-29 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20181219_1514'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-updated']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-updated']},
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]
