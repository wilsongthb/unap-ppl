from django.db import models

# Create your models here.
class Mimetype(models.Model):
    mimetype = models.CharField(max_length=255)

class File(models.Model):
    uploaded_at = models.DateTimeField() # Agregar evento create para guardar automaticamente
    name = models.CharField(max_length=150)
    size = models.PositiveIntegerField(default=0)
    file = models.FileField(upload_to='files')

