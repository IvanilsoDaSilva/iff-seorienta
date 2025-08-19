from django.shortcuts import render
from django.http import HttpResponse

def inicio_nome_app(request):
    return HttpResponse('Inicio do novo app')