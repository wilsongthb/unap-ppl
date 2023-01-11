from django.contrib import admin
from marketplace import models

# Register your models here.
admin.site.register(models.Producto)
admin.site.register(models.Persona)
admin.site.register(models.Categoria)
admin.site.register(models.MapMark)
admin.site.register(models.UnidadMedida)
admin.site.register(models.Publicacion)
admin.site.register(models.Lugar)
