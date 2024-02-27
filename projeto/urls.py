from django.urls import path

from app import views

urlpatterns = [
    path('', views.home),
    path('alunos/', views.alunos, name = 'alunos'),
    path('disciplinas/', views.disciplinas, name ='disciplinas'),
    path('calendario_academico/', views.calendario_academico, name = 'calendario_academico'),
    path('perfil/', views.perfil, name = 'perfil'),
    
    path('pages/alunos/notas/', views.alunos_notas, name= 'notas'),
    path('pages/alunos/desempenho/', views.alunos_desempenho, name= 'desempenho'),
    path('pages/alunos/frequencia/', views.alunos_frequencia, name= 'frequencia'),
    path('pages/alunos/avaliacao/', views.alunos_avaliacao, name= 'avaliacao'),
]
