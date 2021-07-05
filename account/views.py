from django.shortcuts import render, redirect
from django.db import DatabaseError
from .models import user, teacher, create_user_session, create_teacher_session
from datetime import datetime as t


def user_login(request):
    request.session.clear()
    # 로그인 페이지
    if request.method == "GET":
        return render(request, 'log_in.html', {})

    # 로그인 기능
    else:

        # is already registered / login
        try:
            p = user.objects.get(student_number=int(request.POST.get("student_number")))

            if p:
                # not match
                if p.name != request.POST.get("name"):
                    return render(request, 'html/redirect.html', {"error": "학번이랑 이름이 일치하지 않습니다."})

                # login session create
                if create_user_session(request, p.id) != 0:
                    return render(request, 'html/redirect.html', {"error": "로그인 정보를 생성하는 과정에서 오류가 발생했습니다."})

                p.last_login_date = t.now()
                p.save()

        # is not registered / join
        except:
            user.objects.create(
                name=request.POST.get("name"),
                student_number=int(request.POST.get("student_number")),
                homeroom_teacher=teacher.objects.get(id=1),
                joined_date=t.now(),
                last_login_date=t.now(),
            ).save()

            # login session create
            if create_user_session(request, user.objects.get(name=request.POST.get("name"))) != 0:
                return render(request, 'html/redirect.html', {"error": "로그인 정보를 생성하는 과정에서 오류가 발생했습니다."})

    return redirect("index")


def teacher_login(request):
    request.session.clear()
    if request.method == "GET":
        return redirect('login')

    try:
        p = teacher.objects.get(email=request.POST.get("email"))

        # not match
        if p.name != request.POST.get("name"):
            return render(request, 'html/redirect.html', {"error": "학번이랑 이름이 일치하지 않습니다."})

        p.last_login_date = t.now()
        p.save()

    except:
        teacher.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            class_number=0,
            auth=0,
            joined_date=t.now(),
            last_login_date=t.now()
        ).save()

    if create_teacher_session(request, teacher.objects.get(email=request.POST.get("email")).id) != 0:
        return render(request, 'html/redirect.html', {"error": "로그인 정보를 생성하는 과정에서 오류가 발생했습니다."})

    return redirect("index")


def logout(request):
    request.session.clear()
    return render(request, 'html/redirect2.html', {"error": "로그아웃되었습니다."})
