from django.shortcuts import render
from rest_framework import viewsets
from marketplace import models, serializers
# Create your views here.

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = models.Persona.objects.all()
    serializer_class = serializers.PersonaSerializer
