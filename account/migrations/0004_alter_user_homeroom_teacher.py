# Generated by Django 3.2.4 on 2021-07-01 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_student_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='homeroom_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.teacher'),
        ),
    ]
