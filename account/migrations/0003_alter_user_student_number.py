# Generated by Django 3.2.4 on 2021-07-01 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_homeroom_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='student_number',
            field=models.IntegerField(unique=True),
        ),
    ]
