from django.core.management.base import BaseCommand
from ppl import models
from marketplace import models as mk_models
import csv
from django.conf import settings
from coresite import settings as currentsettings
import os
import openpyxl
from openpyxl import load_workbook
import re

class Command(BaseCommand):
    def handle(self, *args, **options):
        seed_materia_prima()
        seed_excel_plantas()

def seed_materia_prima():
    # unidad de medida
    um_litros = mk_models.UnidadMedida.objects.create(nombre="LITROS", simbolo="L")
    # materia prima
    mk_models.Producto.objects.create(nombre="LECHE TIPO A", es_materia_prima=True, 
                       unidad_medida=um_litros, precio=1)
    mk_models.Producto.objects.create(nombre="LECHE TIPO B", es_materia_prima=True, 
                       unidad_medida=um_litros, precio=1)
    mk_models.Producto.objects.create(nombre="LECHE TIPO C", es_materia_prima=True, 
                       unidad_medida=um_litros, precio=1)
    mk_models.Producto.objects.create(nombre="LECHE", es_materia_prima=True, 
                       unidad_medida=um_litros, precio=1)

def seed_excel_plantas():
    wb = load_workbook(filename=currentsettings.env('EXCEL_PPL_FILE'))
    sheet = wb['Georeferencia']
    """
    Leer la hoja Georeferencia y guardar datos en db
    """
    print("claro como no:" + str(sheet['R21'].value))
    c_row = 21
    while c_row <= 37:
        print(str(sheet['B'+str(c_row)].value))
        persona = mk_models.Persona.objects.create(
                tipo='J', 
                ruc=str(sheet['E'+str(c_row)].value),
                razon_social=str(sheet['B'+str(c_row)].value),
                telefono1 = sheet['K'+str(c_row)].value,
                email = sheet['L'+str(c_row)].value,
                )
        lat_temp = re.findall("\d+", sheet['V'+str(c_row)].value)
        lat_temp = "".join(lat_temp)
        lat_temp = lat_temp.replace(".", "", 4)
        lat_temp = lat_temp[:2] + "." + lat_temp[2:]

        lng_temp = re.findall("\d+", sheet['W'+str(c_row)].value)
        lng_temp = "".join(lng_temp)
        lng_temp = lng_temp.replace(".", "", 4)
        lng_temp = lng_temp[:2] + "." + lng_temp[2:]

        map_mark = mk_models.MapMark.objects.create(
                label=persona.razon_social,
                lat=float(lat_temp),
                lng=float(lng_temp),
                type='PL',
                )
        planta = models.Planta.objects.create(
                persona=persona,
                tipo=sheet['C'+str(c_row)].value,
                reg_sanitario= True if  sheet['F'+str(c_row)].value == 'Si' else False,
                marca = sheet['AY'+str(c_row)].value,
                marca_registrada = True if  sheet['G'+str(c_row)].value == 'Si' else False,
                map_mark=map_mark,
                )
        map_mark.instance_id = map_mark.id
        map_mark.save()
        c_row += 1
