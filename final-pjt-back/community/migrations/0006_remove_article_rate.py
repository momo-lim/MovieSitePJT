# Generated by Django 3.2.3 on 2021-11-25 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_alter_article_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='rate',
        ),
    ]