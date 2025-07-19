from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    class Meta:
        db_table = 'Categoria'

class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    preco_unitario = models.FloatField()
    quantidade_estoque = models.IntegerField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Produto'