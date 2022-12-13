from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return str(self.id) + '-' + self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255,null=True)
    precio = models.DecimalField(max_digits=12,decimal_places=2)
    imagen_ref = models.ImageField(upload_to='product_images',null=True)

