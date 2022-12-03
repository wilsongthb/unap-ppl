from django.shortcuts import render
from rest_framework import serializers, viewsets
from ppl import models
# Create your views here.


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Categoria
        fields = ['id','nombre']


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = models.Categoria.objects.all()
    serializer_class = CategoriaSerializer

