# Generated by Django 3.2.4 on 2021-06-10 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_account_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='image',
        ),
    ]
