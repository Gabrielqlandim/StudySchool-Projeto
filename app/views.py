from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as lg

#home
def home(request):
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'pages/home.html')
    else:
        return HttpResponseRedirect('/')
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
            return HttpResponseRedirect('/home')
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

def alunos(request):
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'pages/alunos.html')
    else:
        return HttpResponseRedirect('/')

def disciplinas(request):
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'pages/disciplinas.html')
    else:
        return HttpResponseRedirect('/')

def calendario_academico(request):
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'pages/calendario_academico.html')
    else:
        return HttpResponseRedirect('/')

def perfil(request):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_active:
            return render(request, 'pages/perfil.html')
        else:
            return HttpResponse('Você precisa estar logado!')
    if request.method == 'POST':
        user = User.objects.filter().first()
        logout(request)
        return HttpResponseRedirect('/')

#Alunos
def alunos_notas(request):
    if request.user.is_authenticated and request.user.is_active:
            return render(request, 'pages/alunos/notas.html')
    else:
        return HttpResponseRedirect('/')

def alunos_desempenho(request):
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'pages/alunos/desempenho.html')
    else:
        return HttpResponseRedirect('/')
        

def alunos_frequencia(request):
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'pages/alunos/frequencia.html')
    else:
        return HttpResponseRedirect('/')

def alunos_avaliacao(request):
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'pages/alunos/avaliacao.html')
    else:
        return HttpResponseRedirect('/')

def plataforma(request):
    if request.user.is_authenticated:
        return
    else:
        return HttpResponseRedirect('/')