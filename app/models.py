from django.db import models

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField(min_Length=1,max_Length=120)
    email = models.CharField(min_Length=1,max_Length=120)
    passworld = models.CharField(max_Length=120)

class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.CharField(min_Length=1,max_Length=120)
    idade = models.CharField(min_Length=1,max_Length=120)
    ano = models.CharField(min_Length=1,max_Length=8)
    turma = models.CharField(min_Length=1,max_Length=8)