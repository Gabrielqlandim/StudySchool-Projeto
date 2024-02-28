from django.shortcuts import render


#home
def home(request):
    return render(request, 'pages/home.html')

def alunos(request):
    return render(request, 'pages/alunos.html')

def disciplinas(request):
    return render(request, 'pages/disciplinas.html')

def calendario_academico(request):
    return render(request, 'pages/calendario_academico.html')

def perfil(request):
    return render(request, 'pages/perfil.html')

def cadastro(request):
    return render(request, 'pages/cadastrar_alunos.html')

#Alunos

def alunos_notas(request):
    return render(request, 'pages/alunos/notas.html')

def alunos_desempenho(request):
    return render(request, 'pages/alunos/desempenho.html')

def alunos_frequencia(request):
    return render(request, 'pages/alunos/frequencia.html')

def alunos_avaliacao(request):
    return render(request, 'pages/alunos/avaliacao.html')

def alunos_lista(request):
    return render(request, 'pages/alunos/lista.html')