from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as lg

#login
def login(request):
    if request.method == 'GET':
        return render(request, 'pages/login.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        senha = request.POST.get('senha')
        
        user = authenticate(request,username=name,password=senha)

        if user:
            lg(request, user)
            return render(request, 'pages/home.html')
        else:
            print(user)
            return HttpResponse('email ou senha invalidos')
        
def cadastro_prof(request):
    if request.method == 'GET':
        return render(request, 'pages/cadastro.html' )
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=name).first()

        if user:
            messages.success(request, 'Usuário já existente.')
            return HttpResponseRedirect('/cadastro/')
        else:
            user = User.objects.create_user(username=name,email=email,password=senha)
            user.save()

            messages.success(request, 'Usuário cadastrado!')
        return HttpResponseRedirect('/')
        

#cadastro de aluno
def criar_aluno(request):
    return


#home
def home(request):
    print(request.user.is_authenticated, request.user.is_active)
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'pages/home.html')
    else:
        return HttpResponse('Você precisa estar logado!')

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

def plataforma(request):
    if request.user.is_authenticated:
        return
    else:
        return HttpResponse('Você precisa estar logado!')