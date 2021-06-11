from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime as t

from .models import Account, AccountTch,is_valid


def teacher_signIn(request):
    id = request.POST.get('teacher_id')
    pw = request.POST.get('teacher_name')

    if request.method == "POST":
        try:
            # isNotEmpty
            if id and pw:
                account = AccountTch.objects.get(teacher_id=id)

                # isRegistered
                if account.name == pw:
                    account.last_login = t.now()
                    account.save()

                    request.session['teacher'] = account.id

                    return redirect("../../")

        except: pass

    return redirect('teacher_sign_in')


def signIn(request):
    id = request.POST.get('student_number')
    pw = request.POST.get('student_name')

    if request.method == "GET":
        return render(request, 'signin.html')

    elif request.method == "POST":
        try:
            # isNotEmpty
            if id and pw:

                # isNotRegistered
                if not Account.objects.filter(stuNum=id):
                    Account.objects.create(
                        stuNum=id,
                        name=pw,
                        last_login=t.now(),
                        joined_date=t.now(),
                        tch_id=1,
                        isAdmin=0,
                        isSuperUser=0).save()
                    request.session['user'] = id

                    return redirect('../../')

                else: # login
                    account = Account.objects.get(stuNum=id)

                    # isMatchIdAndPw
                    if account.name == pw:
                        account.last_login = t.now()
                        account.save()

                        request.session['user'] = id

                        return redirect('../../')

        except: pass

        return redirect('sign_in')


@csrf_exempt
def singInCheck(request):
    if request.method == "POST":
        try:
            Account.objects.get(stuNum=int(request.POST.get("stuNum")))
            return JsonResponse({"msg": "successfully"}, status=200)

        except BaseException:
            return JsonResponse({"msg": "unknown value"}, status=400)

    return JsonResponse({"msg": "wrong approach"}, status=404)


def logout(request):
    request.session.clear()

    return redirect('../../')
