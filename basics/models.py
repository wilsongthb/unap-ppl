from django.db import models

# Create your models here.
class Mimetype(models.Model):
    mimetype = models.CharField(max_length=255, unique=True)

class File(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # Agregar evento create para guardar automaticamente
    name = models.CharField(max_length=150)
    size = models.PositiveIntegerField(default=0)
    file = models.FileField(upload_to='files')
    mimetype = models.ForeignKey('Mimetype',on_delete=models.PROTECT)
    #  creator

class AbsModelTimestamps(models.Model):
    """
    Abstract de modelo con created_at y updated_at
    """
    class Meta:
        abstract=True
    created_at = models.DateTimeField(auto_now_add=True) # Agregar evento create para guardar automaticamente
    updated_at = models.DateTimeField(auto_now=True) # Agregar evento create para guardar automaticamente
    deleted_at = models.DateTimeField(null=True, blank=True) # Agregar evento create para guardar automaticamente


class ParametroProceso(models.Model):
    entero1=models.PositiveIntegerField(default=0)
    entero2=models.PositiveIntegerField(default=0)
    entero3=models.PositiveIntegerField(default=0)
    texto1=models.CharField(max_length=100, blank=True, null=True)
    texto2=models.CharField(max_length=100, blank=True, null=True)
    texto3=models.CharField(max_length=100, blank=True, null=True)
    importe1=models.FloatField(blank=True)
    importe2=models.FloatField(blank=True)
    importe3=models.FloatField(blank=True)
    check1=models.BooleanField(blank=True)
    check2=models.BooleanField(blank=True)
    check3=models.BooleanField(blank=True)
