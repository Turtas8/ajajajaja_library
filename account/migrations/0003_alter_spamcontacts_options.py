# Generated by Django 4.1.2 on 2022-10-31 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_spamcontacts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='spamcontacts',
            options={'verbose_name': 'SpamContacts', 'verbose_name_plural': 'SpamContacts'},
        ),
    ]