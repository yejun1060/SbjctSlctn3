from django.shortcuts import render
from django.apps import apps


model = apps.get_model('main', 'Account')


def index(request):
    pk = request.session.get('user')

    if pk:
        account = model.objects.get(stuNum=pk)
        name = account.name

        return render(request, 'index.html', {'pk': pk, 'name': name})

    return render(request, 'index.html')
