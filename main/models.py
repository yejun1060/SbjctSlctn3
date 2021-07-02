import django
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