import django
from django.shortcuts import render
from django.db import models


def user_info_view(request, user):
    array = []

    q = user.objects.get(id=request.session['user_id'])

    for i in str(q.student_number):
        array += i

    # ex)10반
    if array[1] != "0":
        classes = array[1] + array[2]
    else:
        classes = array[2]

    if q.homeroom_teacher.name != "미배정":
        q.homeroom_teacher.name += "선생님"

    value = {"sortation": "0", "name": q.name, "grade": array[0], "class": classes, "homeroom_teacher": q.homeroom_teacher.name}
    print(value)
    return value


def cal_period(request):
    try:
        a = request.POST.getlist("A[]")[0]
        b = request.POST.getlist("B[]")[0]
        c = request.POST.getlist("C[]")[0]
        d = request.POST.getlist("D[]")[0]
        e = request.POST.getlist("E[]")
        h = request.POST.getlist("H[]")[0]

        return a + ";" + b + ";" + c + ";" + d + ";" + e[0] + ";" + e[1] + ";" + e[2] + ";" + h
    
    # 채워지지 않은 값이 있다면
    except IndexError:
        return -2
    # 예상하지 못한 오류
    except BaseException as e:
        print(e)
        print("cal_period 함수 내에서 발생한 오류입니다.")
        return -1


def check_type(request):
    try:
        # 구분이 학생이면
        if request.session.get("sortation") == 0:
            # user table id가 있다면
            if request.session.get("user_id"):
                return 0
            # 예상하지 못한 오류
            else:
                return -1
        # 구분이 선생이면
        elif request.session.get("sortation") == 1:
            # teacher table id가 있다면
            if request.session.get("teacher_id"):
                return 1
            # 예상하지 못한 오류
            else:
                -1
    # 알 수 없는 오류
    except BaseException as e:
        print(e)
        print("check_type 함수 내에서 발생한 오류입니다.")
        return -3