# Generated by Django 4.1.2 on 2022-11-03 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]