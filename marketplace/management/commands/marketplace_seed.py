from django.core.management.base import BaseCommand
import marketplace.models as models
import csv
from django.conf import settings
import os
from openpyxl import load_workbook

class Command(BaseCommand):
    def handle(self, *args, **options):
        #  seed_map_markers()
        seed_lugares()
        seed_productos()


def seed_map_markers():
    with open(os.path.join(settings.BASE_DIR, 'marketplace/data/map-markers.csv'), newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',',quotechar='"')
        i = 1
        for row in spamreader:
            print(row)
            if i > 1:
                models.MapMark.objects.create(
                    label=row[0],
                    title=row[1],
                    lat=row[2],
                    lng=row[3],
                    type=row[4]
                )
            i += 1

def seed_productos():
    with open(os.path.join(settings.BASE_DIR, 'marketplace/data/base_productos.csv'), newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',',quotechar='"')
        i = 1
        unidad_med = models.UnidadMedida.objects.create(
                nombre = 'KILOS',
                simbolo = 'Kg'
                )
        for row in spamreader:
            print(row)
            if i > 1:
                #  models.MapMark.objects.create(
                #      label=row[0],
                #      title=row[1],
                #      lat=row[2],
                #      lng=row[3],
                #      type=row[4]
                #  )

                models.Producto.objects.create(
                        nombre=row[0],
                        precio=row[1],
                        codigo=row[2],
                        es_base=row[3],
                        es_materia_prima=row[4],
                        unidad_medida=unidad_med,
                        )
            i += 1

def seed_lugares():
    wb = load_workbook(os.path.join(settings.BASE_DIR, 'marketplace/data/Ubigeo-ID-Descripción.xlsx'))
    sheet = wb['ubicacionGeografica']
    cont = 2
    while cont <= 2078:
        cod_post = sheet['D' + str(cont)].value
        #  print(cod_post[2:7])
        if cod_post[2:6] == '0000':
            tipo = 'DE'
            nombre = sheet['A' + str(cont)].value[3:]
        elif cod_post[4:6] == '00':
            tipo = 'PR'
            nombre = sheet['B' + str(cont)].value[3:]
        else:
            tipo='DI'
            nombre = sheet['C' + str(cont)].value[3:]

        models.Lugar.objects.create(
                ndep=cod_post[0:2],
                nprov=cod_post[2:4],
                ndist=cod_post[4:6],
                tipo=tipo,
                nombre=nombre)
        cont += 1
