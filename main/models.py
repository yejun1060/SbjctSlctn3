import django
from django.db import models
from django.db.models import PROTECT


class AccountTch(models.Model):
    id = models.AutoField(primary_key=True)
    teacher_id = models.CharField(max_length=20, default="id", unique=True)
    name = models.CharField(max_length=5)
    class_number = models.IntegerField(default=0)

    Auth = models.IntegerField(default=2)

    joined_date = models.DateTimeField(default=django.utils.timezone.now)
    last_login = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.name


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    stuNum = models.IntegerField()
    name = models.CharField(max_length=5)

    tch = models.ForeignKey(AccountTch, on_delete=PROTECT)

    joined_date = models.DateTimeField(default=django.utils.timezone.now)
    last_login = models.DateTimeField(default=django.utils.timezone.now)

    isAdmin = models.CharField(max_length=1, default="0")
    isSuperUser = models.CharField(max_length=1, default="0")

    def __str__(self):
        return self.name
