from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html')

def alunos(request):
    return render(request, 'pages/alunos.html')

def iniciacao_esportiva(request):
    return render(request, 'pages/iniciacao_esportiva.html')

def calendario_academico(request):
    return render(request, 'pages/calendario_academico.html')