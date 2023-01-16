from rest_framework import serializers
from marketplace import models

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Persona
        fields = '__all__'


class UnidadMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UnidadMedida
        fields = '__all__'
        

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Producto
        fields = '__all__'

def get_inst():
    return 'Faaa'

class PublicacionSerializer(serializers.ModelSerializer):
    def get_producto_nombre(self):
        return 'claro como no'

    producto_nombre = serializers.CharField(
            read_only=True, 
            source = 'producto.nombre'
            #  source = 'get_producto_nombre'
            )

    class Meta:
        model = models.Publicacion
        fields = '__all__'


class LugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lugar
        fields = '__all__'


class MapMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MapMark
        fields = '__all__'