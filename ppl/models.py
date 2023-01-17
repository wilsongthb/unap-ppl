from django.db import models
from marketplace.models import Persona, Producto, MapMark
from basics.models import AbsModelTimestamps
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
# Create your models here.


class Planta(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, 
                             null=True, blank=True)
    persona = models.ForeignKey(
            Persona, on_delete=models.PROTECT) # planta requiere definir con una persona
    tipo = models.CharField(max_length=20, null=True) # es A,B o C
    reg_sanitario = models.BooleanField(default=False, 
            help_text="Registro Sanitario") # tiene o no
    marca = models.CharField(max_length=200, null=True)
    marca_registrada = models.BooleanField(default=False)
    map_mark = models.ForeignKey(MapMark, on_delete=models.PROTECT, null=True)


# integrante activo
class PlantaIntegrante(models.Model):
    planta = models.ForeignKey(Planta, on_delete=models.PROTECT)
    integrante = models.ForeignKey(Persona, on_delete=models.PROTECT)
    cargo = models.CharField(max_length=80)
    es_titular = models.BooleanField(default=False)
    class Meta:
        unique_together = ['planta', 'integrante']


class PlantaProveedor(models.Model):
    planta = models.ForeignKey(Planta, on_delete=models.PROTECT)
    proveedor = models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='+')
    map_mark = models.ForeignKey(MapMark, on_delete=models.PROTECT, null=True)
    class Meta:
        unique_together = ['planta', 'proveedor']


class PlantaMovimiento(AbsModelTimestamps):
    planta=models.ForeignKey(Planta, on_delete=models.PROTECT)
    socio=models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='+')
    tipo=models.CharField(max_length=1) # I=Ingreso, E=Egreso
    producto=models.ForeignKey(Producto, on_delete=models.PROTECT, related_name='+')
    fecha=models.DateField(help_text="Fecha del movimiento")
    lote=models.PositiveSmallIntegerField(default=1)
    importe=models.DecimalField(max_digits=14, decimal_places=2,
            help_text="Precio unitario x cantidad")
    cantidad=models.DecimalField(max_digits=14, decimal_places=2,
            help_text="Cantidad en la unida de medida",
            default=1)
    precio_unitario=models.DecimalField(max_digits=14, decimal_places=2, 
            help_text="Precio por unidad",
            validators=[MinValueValidator])
    observacion=models.CharField(max_length=255, null=True)
    fecha_pago=models.DateField(null=True)



class PlantaSaldo(AbsModelTimestamps):
    planta=models.ForeignKey(Planta, on_delete=models.PROTECT, related_name='+')
    socio=models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='+')
    producto=models.ForeignKey(Producto, on_delete=models.PROTECT, related_name='+')
    cantidad=models.DecimalField(max_digits=14, decimal_places=2)
    importe=models.DecimalField(max_digits=14, decimal_places=2)
    precio_un_ta = models.DecimalField(max_digits=14, decimal_places=2, 
            help_text="Precio unitario temporada alta")
    precio_un_tb = models.DecimalField(max_digits=14, decimal_places=2, 
            help_text="Precio unitario temporada baja")
    class Meta:
        unique_together=['planta', 'socio', 'producto']

