from django.db import models
from marketplace.models import Persona
from basics.models import AbsModelTimestamps
from django.core.validators import MinValueValidator
# Create your models here.


class Planta(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    tipo = models.CharField(max_length=20, null=True)
    reg_sanitario = models.BooleanField(default=False)
    marca = models.CharField(max_length=200, null=true)
    marca_registrada = models.BooleanField(default=False)
    nivel = models.CharField(max_length=200, null=True)
    calidad = models.Decimal(max_digits=3, decimal_places=2, default=0)


class PlantaMovimiento(AbsModelTimestamps):
    planta=models.ForeignKey(Planta, on_delete=models.PROTECT)
    Socio=models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='+')
    tipo=models.CharField(max_length=1) # C=Compra, V=Venta
    producto=models.ForeignKey(Producto, on_delete=models.PROTECT, related_name='+')
    fecha=models.DateField()
    lote=models.PositiveSmallIntegerField(default=1)
    importe=models.DecimalField(max_digits=18, decimal_places=2,
            help_text="Precio unitario x cantidad")
    cantidad=models.DecimalField(max_digits=12, decimal_places=2,
            help_text="Cantidad en la unida de medida",
            default=1)
    precio_unitario_org=models.DecimalField(max_digits=18, decimal_places=2, 
            help_text="Precio por unidad originalmente registrado", 
            validators=[MinValueValidator])
    precio_unitario=models.DecimalField(max_digits=18, decimal_places=2, 
            help_text="Precio por unidad",
            validators=[MinValueValidator])
    observacion=models.CharField(max_length=255, null=True)
    fecha_pago=models.DateField(null=True)


class PlantaIntegrantes(models.Model):
    integrante = models.ForeignKey(Persona, on_delete=models.PROTECT)
    cargo = models.CharField(max_length=80)


class PlantaProveedor(models.Model):
    planta = models.ForeignKey(Planta, on_delete=models.PROTECT)
    proveedor = models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='+')


class Saldo(models.Model):
    comprador=models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='+')
    proveedor=models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='+')
    materia_prima=models.ForeignKey(MateriaPrima, on_delete=models.PROTECT, related_name='+')
    cantidad=models.DecimalField(max_digits=12, decimal_places=2)
    importe=models.DecimalField(max_digits=18, decimal_places=2)
    class Meta:
        unique_together=['comprador_id', 'proveedor_id', 'materia_prima_id']

