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


class PublicacionSerializer(serializers.ModelSerializer):
    producto_obj = serializers.SerializerMethodField(read_only=True)
    def get_producto_obj(self, obj):
        return ProductoSerializer(obj.producto).data
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
