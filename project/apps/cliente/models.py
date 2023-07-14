from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class IdiomaPrincipal(models.Model):
    idioma = models.CharField(max_length=20)

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    nacimiento = models.DateField(null=True)
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
    idioma = models.ForeignKey(IdiomaPrincipal, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

