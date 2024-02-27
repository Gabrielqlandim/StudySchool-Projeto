from django.urls import path
from app import views

urlpatterns = [
    path('', views.home),
    path('alunos/', views.alunos, name = 'alunos'),
    path('disciplinas/', views.disciplinas, name ='disciplinas'),
    path('calendario_academico/', views.calendario_academico, name = 'calendario_academico'),
    path('perfil/', views.perfil, name = 'perfil'),

]
