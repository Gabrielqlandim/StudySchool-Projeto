from django.urls import path
from app import views

urlpatterns = [
    path('', views.home),
    path('alunos/', views.alunos),
    path('disciplinas/', views.disciplinas),
    path('calendario_academico/', views.calendario_academico),
    path('perfil/', views.perfil),
    path('perfil/alunos', views.alunos)

]
