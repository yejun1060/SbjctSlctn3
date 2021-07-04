# Generated by Django 3.2.4 on 2021-07-05 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_teacher_email'),
        ('subject', '0003_auto_20210705_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.user', unique=True),
        ),
    ]
