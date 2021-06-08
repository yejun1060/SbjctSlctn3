from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime as t

from .models import Account


def signUp(request):
    if request.method == "GET":
        return render(request, 'unknown/signUp.html')

    elif request.method == "POST":
        try:
            # isRegistered
            if Account.objects.filter(stuNum=request.POST.get('stuNum')).exists():
                return JsonResponse({"msg": "already signed up"}, status=400)

            # HasBlank
            if request.POST.get('stuNum') or request.POST.get('name') == "":
                return JsonResponse({"msg": "value has null"}, status=400)

            # create account
            Account.objects.create(
                stuNum=request.POST.get('stuNum'),
                name=request.POST.get('name')).save()
            return JsonResponse({"msg": "successfully"}, status=200)

        except: return JsonResponse({"msg": "error"}, status=400)


def signIn(request):
    id = request.POST.get('stuNum')
    pw = request.POST.get('name')

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
                        joined_date=t.now()).save()
                    request.session['user'] = id

                    return redirect('../../')

                else: # login
                    # isMatchIdAndPw
                    if Account.objects.get(stuNum=id).name == pw:
                        account = Account.objects.get(stuNum=id)
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

    return redirect('')
