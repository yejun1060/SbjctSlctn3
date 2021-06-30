from django.shortcuts import render, redirect
from django.db import DatabaseError
from .models import user, teacher
from datetime import datetime as t


def login(request):
    if request.method == "POST":

        try:
            if user.objects.get(student_number=request.POST.get("student_number")):
                pass

            query = user.objects.create(
                name=request.POST.get("name"),
                student_number=request.POST.get("student_number"),
                homeroom_teacher=teacher.objects.get(id=1),
                joined_date=t.now(),
                last_login_date=t.now(),
            ).save()

            return redirect('indexs')

        except:
            return render(request, 'html/redirect.html', {})

        return redirect('login')

    return render(request, 'member/join.html', {})
