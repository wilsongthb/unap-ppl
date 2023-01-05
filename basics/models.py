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

class AbsModelTimestamps(models.Model):
    """
    Abstract de modelo con created_at y updated_at
    """
    class Meta:
        abstract=True
    created_at = models.DateTimeField(auto_now_add=True) # Agregar evento create para guardar automaticamente
    updated_at = models.DateTimeField(auto_now=True) # Agregar evento create para guardar automaticamente
    deleted_at = models.DateTimeField(null=True) # Agregar evento create para guardar automaticamente


class ParametroProceso(models.Model):
    secuencia_1=models.PositiveIntegerField(primary_key=True)
    secuencia_2=models.PositiveIntegerField(primary_key=True)
    secuencia_3=models.PositiveIntegerField(primary_key=True)
    descripcion=models.CharField(max_length=60, blank=True)
    importe_1=models.FloatField(max_digits=18, blank=True)
    importe_2=models.FloatField(max_digits=18, blank=True)
    importe_3=models.FloatField(max_digits=18, blank=True)
