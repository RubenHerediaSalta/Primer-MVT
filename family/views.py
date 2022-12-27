from django.shortcuts import render
from django.http import HttpResponse

from family.models import Family

def list_family(request):
    family = Family.objects.all()
    context = {
        'family' : family,
    }
    return render(request, 'family/list_family.html', context=context)

def add_familiar(request):
    Family.objects.create(name='Ruben', age=35, study=True)
    Family.objects.create(name='Lucas', age=37, study=True)
    Family.objects.create(name='Sara', age=39, study=False)
    Family.objects.create(name='Joaquin', age=15, study=True)
    return HttpResponse('Familia Agregada')
