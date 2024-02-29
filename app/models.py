from django.db import models

class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=120)
    idade = models.CharField(max_length=120)
    ano = models.CharField(max_length=8)
    turma = models.CharField(max_length=8)
