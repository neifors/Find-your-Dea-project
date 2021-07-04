from django.db import models
from django.db.models.fields import CharField


class Dea(models.Model):
    codigo_dea = models.CharField(max_length=100)
    direccion_ubicacion = models.CharField(max_length=100)
    direccion_via_codigo = models.CharField(max_length=20, default=None)
    direccion_via_nombre = models.CharField(max_length=100, default=None)
    direccion_portal_numero = models.CharField(max_length=10)
    direccion_codigo_postal = models.CharField(max_length=10, default=None)
    horario_acceso = models.CharField(max_length=90)
    x_utm = models.IntegerField(default=None)
    y_utm = models.IntegerField(default=None)

class User(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    email = models.EmailField(max_length=70)
    pwd = models.CharField(max_length=12)