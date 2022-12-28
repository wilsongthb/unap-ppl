from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from basics.models import File

def user_directory_path(instance, filename):
    return 'products/user_{0}'.format(instance.user.id)

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    imagen_ref = models.ImageField(upload_to='categories/images',null=True,blank=True)
    icon_ref = models.ImageField(upload_to='categories/icons',null=True,blank=True)
    def __str__(self):
        return str(self.id) + '-' + self.nombre

class AbstractProducto(models.Model):
    class Meta:
        abstract=True
    titulo = models.CharField(max_length=50)
    categoria = models.ForeignKey(
            'Categoria',
            on_delete=models.PROTECT)
    imagen_ref = models.ImageField(
            upload_to=user_directory_path,
            null=True,
            blank=True)
    creador = models.ForeignKey(User,on_delete=models.PROTECT)
    #  unidad_medida = models.CharField(max_length=50)

"""
Producto base, este producto no se puede registrar en ventas,
es una entidad para crear productos nuevos para los usuarios publicadores
"""
class BaseProducto(AbstractProducto):
    pass

class Producto(AbstractProducto):
    base_producto = models.ForeignKey(
            'BaseProducto',
            on_delete=models.PROTECT,
            null=True)
    codigo = models.CharField(max_length=30,null=True,blank=True)
    descripcion = models.CharField(max_length=255,null=True)
    precio = models.DecimalField(max_digits=12,decimal_places=2)
    precio_ori = models.DecimalField(
            max_digits=12,
            decimal_places=2,
            null=True)
    cantidad = models.DecimalField(max_digits=12,decimal_places=2,null=True)
    ubicacion_label = models.CharField(max_length=80)
    ubicacion_cod = models.CharField(max_length=10)
    # -25.5342757,-44.1151938
    latitud = models.DecimalField(max_digits=15,decimal_places=9,null=True)
    longitud = models.DecimalField(max_digits=15,decimal_places=9,null=True)
    # Auxiliares
    #  imp_aux1 = models.DecimalField(max_digits=12,decimal_places=2,null=True)
    #  imp_aux2 = models.DecimalField(max_digits=12,decimal_places=2,null=True)


"""
Marcadores de maps
"""
class MapMark(models.Model):
    label = models.CharField(max_length=150)
    title = models.CharField(max_length=255)
    icon_file = models.ForeignKey(File,on_delete=models.PROTECT,null=True,blank=True)
    lat = models.DecimalField(max_digits=18,decimal_places=10)
    lng = models.DecimalField(max_digits=18,decimal_places=10)
    type = models.CharField(max_length=2) # PR: producto, CO: comprador/acopiador
    #  category = models.ForeignKey('Categoria', on_delete=models.PROTECT)
    category = models.ForeignKey()

    
