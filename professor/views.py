from django.shortcuts import render

def inicio(request):
    return render(request, "professor-inicio.html")

def especialidades(request):
    return render(request, "professor-especialidades.html")

def trabalhos(request):
    return render(request, "professor-trabalhos.html")
