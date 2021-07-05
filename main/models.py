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


def teacher_info_view(request, teacher):
    q = teacher.objects.get(id=request.session['teacher_id'])

    value = {"sortation": "1", "name": q.name}
    print(value)

    return value


def cal_period(request):
    # 2학년
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


def cal_period2(request):
    # 3학년 1학기 cal
    try:
        a = request.POST.getlist("A[]")
        j = request.POST.getlist("J[]")[0]

        return a[0] + ";" + a[1] + ";" + a[2] + ";" + a[3] + ";" + a[4] + ";" + a[5] + ";" + a[6] + ";" + a[7] + ";" + a[8] + ";" + j

    # 채워지지 않은 값이 있다면
    except IndexError:
        return -2

    # 예상하지 못한 오류
    except BaseException as e:
        print(e)
        print("cal_period 함수 내에서 발생한 오류입니다.")
        return -1


def cal_period3(request):
    # 3학년 2학기 cal
    try:
        a = request.POST.getlist("A[]")
        j = request.POST.getlist("J[]")[0]

        return a[0] + ";" + a[1] + ";" + a[2] + ";" + a[3] + ";" + a[4] + ";" + a[5] + ";" + a[6] + ";" + a[7] + ";" + j

    # 채워지지 않은 값이 있다면
    except IndexError:
        return -2

    # 예상하지 못한 오류
    except BaseException as e:
        print(e)
        print("cal_period 함수 내에서 발생한 오류입니다.")
        return -1


def sum_control(p1, p2):
    try:
        l = []
        t = ""

        a = p1.split(";")
        for i in range(0, len(a)):
            l.append(a[i])

        a = p2.split(";")
        for i in range(0, len(a)):
            l.append(a[i])

        my_set = set(l)  # 집합set으로 변환
        l = list(my_set)

        for i in range(0, len(l)):
            t += l[i]
            t += ";"

        return t[:len(t)]

    except BaseException as e:
        print(e)
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