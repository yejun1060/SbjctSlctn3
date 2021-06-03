from django.db import models


class Account(models.Model):
    id = models.AutoField(primary_key = True)
    clsNum = models.IntegerField()
    name = models.CharField(max_length=5)
    pw = models.IntegerField()

    def __str__(self):
        return self.name