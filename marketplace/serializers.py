from rest_framework import serializers
from marketplace import models

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Persona
        fields = '__all__'



