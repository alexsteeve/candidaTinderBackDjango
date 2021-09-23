from django.db import models

# Create your models here.

class Partidos(models.Model):
    IdPartido = models.AutoField(primary_key=True)
    SiglaPartido = models.CharField(max_length=100)
    NomePartido = models.CharField(max_length=100)

class Propostas(models.Model):
    IdProposta = models.AutoField(primary_key=True)
    CodigoProposta = models.CharField(max_length=100)
    DataProposta = models.DateField(default='2000-01-01')
    Link1Proposta = models.CharField(max_length=100)
    Link2Proposta = models.CharField(max_length=100)
    Popularidade = models.IntegerField(default=0)
    NomeProposta = models.CharField(max_length=100)

class Usuarios(models.Model):
    IdUsuario = models.AutoField(primary_key=True)
    Login = models.CharField(max_length=100)
    Senha = models.CharField(max_length=100)
    Nome = models.CharField(max_length=100)
    Estado = models.CharField(max_length=100)

class Parlamentares(models.Model):
    IdParlamentar = models.AutoField(primary_key=True)
    NomeParlamentar = models.CharField(max_length=100)
    IdPartido = models.ForeignKey(Partidos, on_delete=models.CASCADE)
    EstadoParlamentar = models.CharField(max_length=100)
    IdParlamentarEleito = models.IntegerField(null=True)

class VotacoesParlamentares(models.Model):
    IdVotacao = models.AutoField(primary_key=True)
    IdParlamentar = models.ForeignKey(Parlamentares, on_delete=models.CASCADE)
    IdProposta = models.ForeignKey(Propostas, on_delete=models.CASCADE)
    Voto = models.CharField(max_length=100)

class VotacoesUsuarios(models.Model):
    IdVotacao = models.AutoField(primary_key=True)
    IdUsuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    IdProposta = models.ForeignKey(Propostas, on_delete=models.CASCADE)
    Voto = models.CharField(max_length=100)