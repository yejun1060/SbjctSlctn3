from django.db import models
from django.http import HttpResponse, Http404
from django.db.models import PROTECT
from datetime import datetime as t


class teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45, default=" ")

    class_number = models.IntegerField()
    auth = models.IntegerField()

    joined_date = models.DateTimeField()
    last_login_date = models.DateTimeField()

    def __str__(self):
        return self.name + "선생님의 계정"


class user(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    student_number = models.IntegerField(unique=True)
    homeroom_teacher = models.ForeignKey(teacher, on_delete=PROTECT)
    
    joined_date = models.DateTimeField()
    last_login_date = models.DateTimeField()
    
    def __str__(self):
        return self.name + "의 계정"


def create_user_session(request, user_id):
    if request.method != "POST":
        raise Http404

    try:
        request.session['sortation'] = 0
        request.session['user_id'] = user_id

        return 0

    except: return -1


def create_teahcer_session(request, teacher_id):
    if request.method != "POST":
        raise Http404

    try:
        request.session['sortation'] = 1
        request.session['teacher_id'] = teacher_id

        return 0

    except: return -1