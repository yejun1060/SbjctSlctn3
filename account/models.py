from django.db import models
from django.db.models import PROTECT


class teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class_number = models.IntegerField()
    auth = models.IntegerField()

    joined_date = models.DateTimeField()
    last_login_date = models.DateTimeField()

    def __str__(self):
        return self.name + "선생님의 계정"


class user(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    student_number = models.IntegerField()
    homeroom_teacher = models.ForeignKey(teacher, on_delete=PROTECT)
    
    joined_date = models.DateTimeField()
    last_login_date = models.DateTimeField()
    
    def __str__(self):
        return self.name + "의 계정"


