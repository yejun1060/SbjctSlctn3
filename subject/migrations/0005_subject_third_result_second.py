# Generated by Django 3.2.4 on 2021-07-06 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0004_alter_subject_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='third_result_second',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
