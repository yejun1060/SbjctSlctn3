from django.shortcuts import render, redirect
from django.db import DatabaseError
from .models import user, teacher, create_user_session, create_teahcer_session
from datetime import datetime as t


def login(request):
    if request.method == "POST":

        try:
            # student join
            if not user.objects.filter(student_number=request.POST.get("student_number")):
                query = user.objects.create(
                    name=request.POST.get("name"),
                    student_number=request.POST.get("student_number"),
                    # homeroom teacher is not assigned
                    homeroom_teacher=teacher.objects.get(id=1),
                    joined_date=t.now(),
                    last_login_date=t.now(),
                ).save()

                return render(request, 'html/redirect2.html', {"error": "회원가입이 완료되었습니다."})

            # student login


            # student login logic

            return redirect('index')

        except BaseException as e:
            print(e)
            return render(request, 'html/redirect.html', {"error": "로그인 과정 중 오류가 발생한 것 같습니다."})

        return redirect('login')

    return render(request, 'login.html', {})
