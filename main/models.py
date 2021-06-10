import django
from django.db import models
from django.db.models import PROTECT


class AccountTch(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=5)

    Auth = models.IntegerField(default=1)

    joined_date = models.DateField(default=django.utils.timezone.now)
    last_login = models.DateField(default=django.utils.timezone.now)

    def __str__(self):
        return self.name


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    stuNum = models.IntegerField(unique=True)
    name = models.CharField(max_length=5)

    tch = models.ForeignKey(AccountTch, on_delete=PROTECT)

    joined_date = models.DateField(default=django.utils.timezone.now)
    last_login = models.DateField(default=django.utils.timezone.now)

    isAdmin = models.CharField(max_length=1, default="0")
    isSuperUser = models.CharField(max_length=1, default="0")

    def __str__(self):
        return self.name


