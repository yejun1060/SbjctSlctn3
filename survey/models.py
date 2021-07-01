from django.db import models
from account.models import teacher, user
from django.db.models import PROTECT


class survey(models.Model):
    id = models.IntegerField(primary_key=True)
    survey_name = models.CharField(max_length=45)
    teacher_id = models.ForeignKey(teacher, on_delete=PROTECT)
    opened_date = models.DateField()
    closed_date = models.DateField()

    def __str__(self):
        return self.survey_name


class second_select(models.Model):
    id = models.IntegerField(primary_key=True)
    survey_id = models.ForeignKey(survey, on_delete=PROTECT)
    first = models.CharField(max_length=45, null=True)
    second = models.CharField(max_length=45, null=True)
    third = models.CharField(max_length=45, null=True)
    four = models.CharField(max_length=45, null=True)
    five = models.CharField(max_length=45, null=True)
    user_id = models.ForeignKey(user, on_delete=PROTECT)
    
    def __str__(self):
        return self.user_id + "의 선택결과(2학년)"


class third_select(models.Model):
    id = models.IntegerField(primary_key=True)
    survey_id = models.ForeignKey(survey, on_delete=PROTECT)
    first = models.CharField(max_length=45, null=True)
    second = models.CharField(max_length=45, null=True)
    third = models.CharField(max_length=45, null=True)
    four = models.CharField(max_length=45, null=True)
    five = models.CharField(max_length=45, null=True)
    user_id = models.ForeignKey(user, on_delete=PROTECT)

    def __str__(self):
        return self.user_id + "의 선택결과(3학년)"
