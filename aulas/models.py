from django.db import models

# Create your models here.

class Diagnostico(model.Model):
    tratamento_recomendado = models.CharField(max_length=80)
    observacao = models.CharField(max_length=999)
    medicacao = models.CharField(max_length=80)
    id_animal = models.IntegerField
