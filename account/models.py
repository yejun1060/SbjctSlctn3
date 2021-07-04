from django.db import models
from django.http import Http404
from django.db.models import PROTECT


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
    homeroom_teacher = models.ForeignKey(teacher, on_delete=PROTECT, null=True)
    
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

        print("user session이 생성되었습니다.")
        return 0

    except: return -1


def create_teacher_session(request, teacher_id):
    try:
        request.session['sortation'] = 1
        request.session['teacher_id'] = teacher_id

        print("teacher session이 생성되었습니다.")
        return 0

    except:
        print(-1)
        return -1