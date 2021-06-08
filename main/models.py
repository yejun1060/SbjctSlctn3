import django
from django.db import models


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    stuNum = models.IntegerField(unique=True)
    name = models.CharField(max_length=5)
    joined_date = models.DateField(default=django.utils.timezone.now)
    last_login = models.DateField(default=django.utils.timezone.now)

    def __str__(self):
        return self.name
