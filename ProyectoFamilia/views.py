from django.http import HttpResponse
from django.shortcuts import render

def hola_mundo(request):
    return HttpResponse('HOLA MUNDO')

def hola_desde_template(request):
    return render(request, 'hola.html', context={})