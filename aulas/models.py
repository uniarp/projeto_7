from django.db import models

# Create your models here.

class Diagnostico(models.Model):
    motivo_atendimento = models.CharField(max_length=80)
    observacao = models.CharField(max_length=80)
    id_animal = models.IntegerField()
    data_hora = models.DateTimeField("date published")
