from django.shortcuts import render
from django.apps import apps


def index(request):
    temp = 'index.html'

    pk = request.session.get('user')
    model = apps.get_model('main', 'Account')
    model2 = apps.get_model('main', 'AccountTch')

    if pk:
        account = model.objects.get(stuNum=pk)
        tch = model2.objects.get(id=account.tch_id)
        
        if tch.name != "미배정":
            tch.name += "선생님"
        
        return render(request, temp, {'pk': pk, 'name': account.name, 'tch': tch.name})

    return render(request, temp)
