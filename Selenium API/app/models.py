from django.db import models

# Create your models here.

class Sales(models.Model):
    cidade = models.CharField(max_length=150)
    endereço = models.CharField(max_length=150)
    ano = models.IntegerField()