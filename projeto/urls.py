from django.urls import path
from app import views

urlpatterns = [
    path('', views.home),
    path('alunos/', views.alunos),
    path('iniciacao_esportiva/', views.iniciacao_esportiva),
    path('calendario_academico/', views.calendario_academico)
]
