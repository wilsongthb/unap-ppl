from django.db import models
from django.contrib.auth.models import User
from basics.models import AbsModelTimestamps
# Create your models here.


class Persona(models.Model):
    """
    Tabla de datos personales de usuarios
    """
    class Meta:
        indexes=[
            models.Index(fields=['tipo', 'dni', 'ruc']),
            models.Index(fields=['nombres', 'ap_paterno', 'ap_materno', 'razon_social']),
            models.Index(fields=['ndep', 'nprov', 'ndist']),
        ]
    tipo = models.CharField(max_length=1) # F: Fisica, J: Juridica
    dni = models.CharField(max_length=8, null=True)
    ruc = models.CharField(max_length=11, null=True)
    nombre_completo = models.CharField(max_length=255)
    ap_paterno = models.CharField(max_length=50, null=True)
    ap_materno = models.CharField(max_length=50, null=True)
    nombres = models.CharField(max_length=200)
    sexo = models.CharField(max_length=1, 
            help_text='F: Femenino, M: Masculino, N: Ninguno', default='N')
    fecha_nacimiento = models.DateField(null=True)
    razon_social = models.CharField(max_length=255, null=True)
    ndep = models.CharField(max_length=2, null=True, help_text="Codigo departamento")
    nprov = models.CharField(max_length=2, null=True, help_text="Codigo Provincia")
    ndist = models.CharField(max_length=2, null=True, help_text="Codigo Distrito")
        # departamento char(2), provincia char(2), distrito char(2)
    direccion = models.CharField(max_length=150, null=True)
    lat_ubi = models.DecimalField(max_digits=18,decimal_places=10, null=True, 
            help_text="Latitud de ubicacion")
    lng_ubi = models.DecimalField(max_digits=18,decimal_places=10, null=True,
            help_text="Longitud de ubicacion")
    telefono1 = models.CharField(max_length=30) # celular principal
    telefono2 = models.CharField(max_length=30, null=True) # numero de celular secundario
    email = models.CharField(max_length=255, null=True)
    foto_perfil = models.ImageField(upload_to='personas/foto_perfil', 
            null=True, blank=True)
    user_id  = models.PositiveBigIntegerField(unique=True, null=True)
    visible = models.BooleanField(default=True) # visible 
    def __str__(self):
        if self.tipo == 'J' and self.razon_social is not None:
            return self.razon_social
        elif self.tipo == 'F':
            return f"{self.nombres} {self.ap_paterno} {self.ap_materno}"
        else:
            return f"{self.id} {self.nombre_completo}"
        

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

class UnidadMedida(models.Model):
    nombre = models.CharField(max_length=20)
    simbolo = models.CharField(max_length=5, null=True)
    def __str__(self):
        return self.nombre
    class Meta:
        unique_together = ['nombre', 'simbolo']


class MapMark(models.Model):
    """
    Marcadores de mapas
    """
    label = models.CharField(max_length=150)
    title = models.CharField(max_length=255)
    icon_file = models.ImageField(upload_to='map_markers/icons', null=True, blank=True)
    lat = models.DecimalField(max_digits=18,decimal_places=10)
    lng = models.DecimalField(max_digits=18,decimal_places=10)
    type = models.CharField(max_length=2) # PR: producto, CO: comprador/acopiador, IN: Institucion
    instance_id = models.PositiveBigIntegerField(null=True)
    visible = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.label} {self.lat} {self.lng}" 


class Producto(AbsModelTimestamps):
    """
    Productos de los usuarios
    """
    nombre = models.CharField(max_length=50)
    imagen_ref = models.ImageField(
            upload_to='productos/images',
            null=True,blank=True)
    es_base = models.BooleanField(default=False) # Define si se pueden crear nuevos productos a partir de este de forma publica
    base_id = models.PositiveBigIntegerField(null=True) # id de producto del producto base
    es_materia_prima = models.BooleanField(default=False)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.PROTECT)
    codigo = models.CharField(max_length=30,null=True,blank=True)
    descripcion = models.CharField(max_length=255,null=True)
    precio = models.DecimalField(max_digits=12,decimal_places=2) # se sobre entiende precio unitario
    visible = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.nombre} x {self.unidad_medida}"


class Publicacion(AbsModelTimestamps):
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    map_mark = models.ForeignKey(MapMark, on_delete=models.PROTECT)
    precio_original = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    precio = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    mostrar_pre_org = models.BooleanField(default=True, 
        help_text="Mostrar precio original")
    cantidad = models.DecimalField(max_digits=14, decimal_places=2, default=1, 
        help_text="Cantidad disponible")


class Lugar(models.Model):
    ndep = models.CharField(max_length=2)
    nprov = models.CharField(max_length=2, default='00')
    ndist = models.CharField(max_length=2, default='00')
    nlugar = models.CharField(max_length=2, default='00')
    tipo = models.CharField(max_length=2) # DE: Departamento, PR: Provincia, DI: Distrito, CO: Comunidad, BA: Barrio
    nombre = models.CharField(max_length=150)
    class Meta:
        unique_together = ['ndep', 'nprov', 'ndist', 'nlugar', 'tipo']
        indexes = [
                models.Index(fields=['ndep', 'nprov', 'ndist', 'nlugar', 'tipo'])
                ]
