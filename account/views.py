from django.shortcuts import render, redirect
from django.db import DatabaseError
from .models import user, teacher
from datetime import datetime as t


def login(request):
    if request.method == "POST":

        try:
            # student login
            if user.objects.filter(student_number=request.POST.get("student_number")):
                pass

            # student join
            query = user.objects.create(
                name=request.POST.get("name"),
                student_number=request.POST.get("student_number"),
                # homeroom teacher is not assigned
                homeroom_teacher=teacher.objects.get(id=1),
                joined_date=t.now(),
                last_login_date=t.now(),
            ).save()

            # student login logic

            return redirect('index')

        except:
            return render(request, 'html/redirect.html', {"error": "로그인 과정 중 오류가 발생한 것 같습니다."})

        return redirect('login')

    return render(request, 'member/join.html', {})
