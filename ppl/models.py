from django.db import models
from marketplace.models import Persona
from basics.models import AbsModelTimestamps
from django.core.validators import MinValueValidator
# Create your models here.

class MateriaPrima(models.Model):
    nombre = models.CharField(max_length=200)
    unidad_medida = models.CharField(max_length=80)
    class Meta:
        unique_together=['nombre','unidad_medida']
    def __str__(self):
        return self.nombre + ' x ' + self.unidad_medida

class Movimiento(AbsModelTimestamps):
    comprador=models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='+')
    proveedor=models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='+')
    materia_prima=models.ForeignKey(MateriaPrima, on_delete=models.PROTECT, related_name='+')
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

class Saldo(models.Model):
    comprador=models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='+')
    proveedor=models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='+')
    materia_prima=models.ForeignKey(MateriaPrima, on_delete=models.PROTECT, related_name='+')
    cantidad=models.DecimalField(max_digits=12, decimal_places=2)
    importe=models.DecimalField(max_digits=18, decimal_places=2)
    class Meta:
        unique_together=['comprador_id', 'proveedor_id', 'materia_prima_id']

