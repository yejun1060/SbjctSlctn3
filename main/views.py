from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

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
            return JsonResponse({"msg": "successfully"}, status= 200)

        except BaseException as e:
            return JsonResponse({"msg": e}, status=400)


def signIn(request):
    if request.method == "GET":
        return render(request, temp4)

    elif request.method == "POST":
        pass


def singInCheck(request):
    if request.method == "POST":
        try:
            account = Account.objects.get(clsNum= request.POST.get("clsNum"))
            return JsonResponse({"msg": "successfully"}, status=200)

        except Account.objects.get(clsNum= request.POST.get("clsNum")).DoesNotExist:
            return JsonResponse({"msg": "unknown value"}, status=400)

    else:
        return JsonResponse({"msg": "wrong approach"}, status= 404)


# function
def insert(request):
    clsNum = int(request.POST.get('clsNum'))
    name = request.POST.get('name')
    pw = 1544

    Account(clsNum=clsNum, name=name, pw=pw).save()

    return redirect("../v")
