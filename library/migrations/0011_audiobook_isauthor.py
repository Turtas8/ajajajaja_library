# Generated by Django 4.1.2 on 2022-11-06 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_book_isauthor'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiobook',
            name='isAuthor',
            field=models.BooleanField(default=False),
        ),
    ]
