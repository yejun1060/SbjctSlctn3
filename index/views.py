from django.shortcuts import render
from django.apps import apps


def index(request):
    pk = request.session.get('user')
    model = apps.get_model('main', 'Account')

    if pk:
        account = model.objects.get(stuNum=pk)
        name = account.name
        tch = account.tch + "선생님"

        if not tch:
            tch = "미배정"
        
        return render(request, 'index.html', {'pk': pk, 'name': name, 'tch': tch})

    return render(request, 'index.html')
