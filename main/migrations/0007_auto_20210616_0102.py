# Generated by Django 3.2.4 on 2021-06-16 01:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210616_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='joined_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
