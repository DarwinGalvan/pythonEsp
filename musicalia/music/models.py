from django.db import models

class Cancion(models.Model):
    nombreartista = models.CharField(blank=False, null=False,max_length=100)
    letra = models.CharField(blank=False, null=False,max_length=100)

