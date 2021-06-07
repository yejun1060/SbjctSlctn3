from django.shortcuts import render


temp1 = "index/index.html"


def index(request):
    return render(request, temp1)