# Generated by Django 4.2.1 on 2023-06-13 06:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_alter_article_authorpost_delete_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='subscribers',
            field=models.ManyToManyField(related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
    ]
