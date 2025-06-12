from django.utils import timezone
from django.db import models
    
    
class Genero(models.Model):
    nome = models.CharField(max_length=50)
    data_cadastro = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.nome

# nome, ano_do_filme, estudio, genero, sinopse, data_cadastro, imagem, diretor, comentario, atores
class Filme(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.DateField(default=timezone.now)
    estudio = models.CharField(max_length=50)
    # genero = models.CharField(max_length=50)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True, blank=True)
    sinopse = models.TextField()
    data_cadastro = models.DateField(default=timezone.now)
    publicado = models.BooleanField(default=True)
    def __str__(self):
        return self.nome
