from django.db import models

# Create your models here.

class UsoModel(models.Model):
    motorista = models.CharField(max_length=100)
    veiculo = models.CharField(max_length=100)
    data_uso = models.DateField()
    horario_inicio = models.TimeField()
    horario_final = models.TimeField()
    km_inicial = models.IntegerField()
    km_final = models.IntegerField()
    destino = models.CharField(max_length=200)
    data_criacao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.motorista
    
class VeiculoModels(models.Model):
    nome = models.CharField(max_length=100)
    placa = models.CharField(max_length=7)
    marca = models.CharField(max_length=50)
    ano = models.IntegerField()
    cor = models.CharField(max_length=30)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
class MotoristaModel(models.Model):
    nome = models.CharField(max_length=100)
    cnh = models.CharField(max_length=20)
    re = models.IntegerField()
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    