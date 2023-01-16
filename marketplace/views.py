from django.shortcuts import render
from rest_framework import viewsets
from marketplace import models, serializers
# Create your views here.

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = models.Persona.objects.all()
    serializer_class = serializers.PersonaSerializer
    search_fields = ['nombre']
    filterset_fields = ['tipo', 'dni', 'ruc', 'ndep', 'nprov', 'ndist']


class UnidadMedidaViewSet(viewsets.ModelViewSet):
    queryset = models.UnidadMedida.objects.all()
    serializer_class = serializers.UnidadMedidaSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = models.Producto.objects.all()
    serializer_class = serializers.ProductoSerializer
    search_fields = ['nombre']


class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = models.Publicacion.objects.all()
    serializer_class = serializers.PublicacionSerializer


class LugarViewSet(viewsets.ModelViewSet):
    queryset = models.Lugar.objects.all()
    serializer_class = serializers.LugarSerializer
    filterset_fields = ['ndep', 'nprov', 'ndist', 'tipo']
    search_fields = ['nombre']


class MapMarkViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MapMarkSerializer
    queryset = models.MapMark.objects.all()
    search_fields = ['label']