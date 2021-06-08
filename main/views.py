from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

from .models import Account

temp1 = "main/index1.html"
temp2 = "main/index2.html"
temp3 = "main/signup.html"
temp4 = "main/signin.html"


def signUp(request):
    if request.method == "GET":
        return render(request, temp3)

    elif request.method == "POST":
        try:
            # isRegistered?
            if Account.objects.filter(clsNum=request.POST.get('clsNum')).exists():
                return JsonResponse({"msg": "already signed up"}, status=400)

            # HasBlank?
            if request.POST.get('clsNum') or request.POST.get('name') == "":
                return JsonResponse({"msg": "value has null"}, status=400)

            # create account
            Account.objects.create(
                clsNum=request.POST.get('clsNum'),
                name=request.POST.get('name'),
                pw=2828).save()
            return JsonResponse({"msg": "successfully"}, status=200)

        except: return JsonResponse({"msg": e}, status=400)


def signIn(request):
    id = request.POST.get('clsNum')
    pw = request.POST.get('name')

    if request.method == "GET":
        return render(request, temp4)

    elif request.method == "POST":
        try:
            account = Account.objects.filter(clsNum=id, name=pw)
            print(account)
            return JsonResponse({"msg": "로그인 성공"}, status=200)

        except: return JsonResponse({"msg": "아이디나 비밀번호를 찾을 수 없습니다."}, status=400)


@csrf_exempt
def singInCheck(request):
    if request.method == "POST":
        try:
            Account.objects.get(clsNum=int(request.POST.get("clsNum")))
            return JsonResponse({"msg": "successfully"}, status=200)

        except BaseException:
            return JsonResponse({"msg": "unknown value"}, status=400)

    return JsonResponse({"msg": "wrong approach"}, status=404)


# function
def insert(request):
    clsNum = int(request.POST.get('clsNum'))
    name = request.POST.get('name')
    pw = 1544

    Account(clsNum=clsNum, name=name, pw=pw).save()

    return redirect("../v")
