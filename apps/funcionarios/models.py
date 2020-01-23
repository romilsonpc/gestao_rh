from django.db import models


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)