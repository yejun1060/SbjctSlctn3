from django.shortcuts import render, redirect
from django.apps import apps


def index(request):
    student_model = apps.get_model('main', 'Account')
    teacher_model = apps.get_model('main', 'AccountTch')

    session1 = request.session.get('user')
    session2 = request.session.get('teacher')

    value = {}

    try:
        if session1:
            pk = request.session.get('user')

            student_account = student_model.objects.get(stuNum=pk)
            teacher = teacher_model.objects.get(id=student_account.tch_id)

            if teacher.name != "미배정":
                teacher.name += "선생님"

            value = {'pk': student_account.stuNum,
                     'student_name': student_account.name,
                     'tch': teacher.name}

        if session2:
            pk = request.session.get('teacher')

            teacher_account = teacher_model.objects.get(id=pk)
            q1 = str(teacher_account.class_number)
            l = []
            
            if q1 == "0":
                q1 = "미배정"

            else:
                for i in q1:
                    l.append(i)

                if l[1] == "0":
                    l[1] = ""
                
                q1 = l[0] + "학년 " + l[1] + l[2] + "반"

            value = {'teacher_pk': pk,
                     'teacher_name': teacher_account.name,
                     'class': q1}

    except: pass

    return render(request, 'index.html', value)
