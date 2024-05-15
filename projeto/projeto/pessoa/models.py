from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=18)

class PessoaJuridica(models.Model):
    cnpj = models.CharField(max_length=100)
    salario = models.FloatField()
    quantFilhos = models.IntegerField()
    quantEmpregados = models.IntegerField()


            