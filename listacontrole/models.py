from django.db import models

class Empresas(models.TextChoices):
    DOPTEX = "Doptex"
    TECELAGEM = "São João Tecelagem"
    TINTURARIA = "São João Tinturaria"
    CORRADI = "Corradi"
    TEXTIL = "Textil Da Serra"
    
class MotoristaModel(models.Model):
    nome = models.CharField(max_length=100)
    cnh = models.CharField(max_length=20)
    re = models.IntegerField()
    empresa = models.CharField(choices=Empresas.choices, default=Empresas.DOPTEX)
    cargo = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
class VeiculoModels(models.Model):
    nome = models.CharField(max_length=100)
    placa = models.CharField(max_length=7)
    marca = models.CharField(max_length=50)
    ano = models.IntegerField()
    cor = models.CharField(max_length=30)
    status = models.BooleanField(default=True)  # True = Disponível, False = Em uso
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
class UsoModel(models.Model):
    motorista = models.ForeignKey(MotoristaModel, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(VeiculoModels, on_delete=models.CASCADE)
    data_uso = models.DateField()
    horario_inicio = models.TimeField()
    horario_final = models.TimeField(null=True, blank=True)
    km_inicial = models.IntegerField()
    km_final = models.IntegerField(null=True, blank=True)
    destino = models.CharField(max_length=200)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.motorista.nome} - {self.veiculo.nome}"