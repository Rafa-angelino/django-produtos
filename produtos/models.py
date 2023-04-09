from django.db import models

# Create your models here.
class Produtos(models.Model):
    cod_prod =models.PositiveIntegerField()
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150)
    barra = models.CharField(max_length=50)
    valor = models.FloatField()
    estoque = models.FloatField()
    
    def __str__(self):
        return f'Produto: {self.nome} : {self.valor}'