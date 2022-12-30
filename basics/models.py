from django.db import models

# Create your models here.
class Mimetype(models.Model):
    mimetype = models.CharField(max_length=255, unique=True)

class File(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # Agregar evento create para guardar automaticamente
    name = models.CharField(max_length=150)
    size = models.PositiveIntegerField(default=0)
    file = models.FileField(upload_to='files')
    mimetype = models.ForeignKey('Mimetype',on_delete=models.PROTECT)
    # def __str__(self):
    #     return self.file
