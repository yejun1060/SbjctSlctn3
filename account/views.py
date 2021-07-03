from django.shortcuts import render, redirect
from django.db import DatabaseError
from .models import user, teacher, create_user_session, create_teahcer_session
from datetime import datetime as t


def user_login(request):
    if request.method == "POST":

        try:
            users, created = user.objects.get_or_create(student_number=request.POST.get("student_number"))
            q = user.objects.get(student_number=request.POST.get("student_number"))

            # join
            if created:

                user.objects.create(
                    name=request.POST.get("name"),
                    student_number=request.POST.get("student_number"),
                    homeroom_teacher=teacher.objects.get(id=1),
                    joined_date=t.now(),
                    last_login_date=t.now()
                ).save()

            # login
            else:

                if not q.name == request.POST.get("name"):
                    return render(request, 'html/redirect.html', {"error": "아이디랑 비밀번호가 일치하지 않습니다."})

            # 로그인 세션 생성
            if create_user_session(request, q.id) != 0:

                return render(request, 'html/redirect.html', {"error": "로그인 정보를 생성하는 과정에서 오류가 발생했습니다."})

            return redirect('index')

        except BaseException as e:
            print(e)
            return render(request, 'html/redirect.html', {"error": "오류가 발생했습니다. 잠시 후 다시 시도해주세요."})

    return render(request, 'login.html', {})


def teacher_login(request):
    pass


def logout(request):
    request.session.clear()
    return render(request, 'html/redirect2.html', {"error": "로그아웃되었습니다."})