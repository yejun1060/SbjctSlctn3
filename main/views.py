from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime as t

from .models import Account, AccountTch


def login(request):
    if request.method == "POST":

        try:
            id = request.POST.get('student_number')
            pw = request.POST.get('student_name')
            q = Account.objects.get(stuNum=id)

            # Yet
            if not q:
                query = Account.objects.create(
                    stuNum=id,
                    name=pw,
                    last_login=t.now(),
                    joined_date=t.now(),
                    tch_id=1,
                    isAdmin=0,
                    isSuperUser=0).save()

            # Not Yet
            else:
                q.last_login = t.now()
                q.save()

            request.session['user'] = id

            return redirect('indexs')

        except: pass

        return redirect('login')

    return render(request, "signin.html", {})


def teacher_login(request):
    if request.method == "POST":

        try:
            id = request.POST.get('teacher_id')
            pw = request.POST.get('teacher_name')

            # isNotEmpty
            if id and pw:
                query = AccountTch.objects.get(teacher_id=id)

                # isRegistered
                if query.name == pw:
                    query.last_login = t.now()
                    query.save()

                    request.session['teacher'] = query.id

                    return redirect("indexs")

        except BaseException as e:print(e)

        return redirect('teacher_login')

    return render(request, "signin.html", {})


def logout(request):
    request.session.clear()

    return redirect('../../')
