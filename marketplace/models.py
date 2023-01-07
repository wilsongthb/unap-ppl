from django.db import models
from django.contrib.auth.models import User
from basics.models import AbsModelTimestamps
# Create your models here.

class Persona(models.Model):
    """
    Tabla de datos personales de usuarios
    """
    tipo = models.CharField(max_length=1) # F: Fisica, J: Juridica
    nombre_completo = models.CharField(max_length=255)
    ap_paterno = models.CharField(max_length=50, null=True)
    ap_materno = models.CharField(max_length=50, null=True)
    nombres = models.CharField(max_length=200)
    razon_social = models.CharField(max_length=255, null=True)
    dni = models.CharField(max_length=8, null=True)
    ruc = models.CharField(max_length=12, null=True)
    ubicacion = models.CharField(max_length=6) # departamento char(2), provincia char(2), distrito char(2)
    direccion = models.CharField(max_length=150, null=True)
    lat_ubi = models.DecimalField(max_digits=18,decimal_places=10, null=True, 
            help_text="Latitud de ubicacion por defecto")
    lng_ubi = models.DecimalField(max_digits=18,decimal_places=10, null=True,
            help_text="Longitud de ubicacion por defecto")
    telefono1 = models.CharField(max_length=30) # celular principal
    telefono2 = models.CharField(max_length=30, null=True) # numero de celular secundario
    foto_perfil = models.ImageField(upload_to='personas/foto_perfil', 
            null=True, blank=True)
    user_id  = models.PositiveBigIntegerField(unique=True, null=True)
    visible = models.BooleanField(default=True) # visible 

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    imagen_ref = models.ImageField(
            upload_to='categorias/images',
            null=True,blank=True)
    icon_ref = models.ImageField(
            upload_to='categorias/icons',
            null=True,blank=True)
    visible=models.BooleanField(default=True)
    def __str__(self):
        return str(self.id) + '-' + self.nombre

class Producto(AbsModelTimestamps):
    """
    Productos de los usuarios
    """
    titulo = models.CharField(max_length=50)
    categoria = models.ForeignKey(
            'Categoria',
            on_delete=models.PROTECT)
    imagen_ref = models.ImageField(
            upload_to='productos/images',
            null=True,blank=True)
    creador = models.ForeignKey(User,on_delete=models.PROTECT)
    es_base = models.BooleanField(default=False) # Define si se pueden crear nuevos productos a partir de este de forma publica
    base_id = models.PositiveBigIntegerField(null=True) # id de producto del producto base
    codigo = models.CharField(max_length=30,null=True,blank=True)
    descripcion = models.CharField(max_length=255,null=True)
    precio = models.DecimalField(max_digits=12,decimal_places=2)
    cantidad = models.DecimalField(max_digits=12,decimal_places=2,null=True)
    map_mark = models.ForeignKey('MapMark', on_delete=models.PROTECT)
    visible = models.BooleanField(default=True) # visible en internet



class MapMark(models.Model):
    """
    Marcadores de mapas
    """
    label = models.CharField(max_length=150)
    title = models.CharField(max_length=255)
    icon_file = models.ImageField(upload_to='map_markers/icons', null=True, blank=True)
    lat = models.DecimalField(max_digits=18,decimal_places=10)
    lng = models.DecimalField(max_digits=18,decimal_places=10)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    type = models.CharField(max_length=2) # PR: producto, CO: comprador/acopiador, IN: Institucion
    instance_id = models.PositiveBigIntegerField(null=True)
    visible = models.BooleanField(default=True)
