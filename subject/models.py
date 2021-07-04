from django.db import models
from django.db.models import PROTECT

from account.models import user


class subject(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(user, on_delete=PROTECT, unique=True)
    second_result = models.CharField(max_length=100, null=True)
    third_result = models.CharField(max_length=100, null=True)
    second_period = models.CharField(max_length=45, null=True)
    third_period = models.CharField(max_length=45, null=True)
    date = models.DateTimeField()
    
    def __str__(self):
        return self.user_id + "의 과목선택 값"
