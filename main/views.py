from django.shortcuts import render
from django.http import HttpResponse
from .models import Account


def index(request):
    template_name = "index2.html"
    value = Account.objects.all()

    return render(request, template_name, {"value": value})


def insert(request):
    clsNum = int(request.GET.get('clsNum'))
    name = request.GET.get('name')
    pw = 1544

    Account(clsNum=clsNum, name=name, pw=pw).save()

    return index(request)
