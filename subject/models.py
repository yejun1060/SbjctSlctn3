from django.db import models
from django.db.models import PROTECT

from account.models import user


class subject(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(user, on_delete=PROTECT)
    result = models.CharField(max_length=100, null=True)
    period = models.CharField(max_length=45, null=True)
    year = models.IntegerField(default=1)
    semester = models.IntegerField(default=0)
    date = models.DateTimeField()
    
    def __str__(self):
        return self.user_id + "의 과목선택 값"
