from django.db import models

# Create your models here.

class Tratamento(models.Model):
    tratamento_recomendado = models.CharField(max_length=80)
    medicacao =  models.CharField(max_length=80)
    fisioterapia = models.CharField(max_length=3)
    castracao = models.CharField(max_length=3)