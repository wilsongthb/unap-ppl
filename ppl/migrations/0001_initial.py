# Generated by Django 4.1.3 on 2023-01-10 12:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20, null=True)),
                ('reg_sanitario', models.BooleanField(default=False, help_text='Registro Sanitario')),
                ('marca', models.CharField(max_length=200, null=True)),
                ('marca_registrada', models.BooleanField(default=False)),
                ('map_mark', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='marketplace.mapmark')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='marketplace.persona')),
            ],
        ),
        migrations.CreateModel(
            name='PlantaProveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map_mark', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='marketplace.mapmark')),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ppl.planta')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='marketplace.persona')),
            ],
        ),
        migrations.CreateModel(
            name='PlantaMovimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('tipo', models.CharField(max_length=1)),
                ('fecha', models.DateField(help_text='Fecha del movimiento')),
                ('lote', models.PositiveSmallIntegerField(default=1)),
                ('importe', models.DecimalField(decimal_places=2, help_text='Precio unitario x cantidad', max_digits=14)),
                ('cantidad', models.DecimalField(decimal_places=2, default=1, help_text='Cantidad en la unida de medida', max_digits=14)),
                ('precio_unitario', models.DecimalField(decimal_places=2, help_text='Precio por unidad', max_digits=14, validators=[django.core.validators.MinValueValidator])),
                ('observacion', models.CharField(max_length=255, null=True)),
                ('fecha_pago', models.DateField(null=True)),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ppl.planta')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='marketplace.producto')),
                ('socio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='marketplace.persona')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlantaIntegrante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=80)),
                ('integrante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='marketplace.persona')),
            ],
        ),
        migrations.CreateModel(
            name='PlantaSaldo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=14)),
                ('importe', models.DecimalField(decimal_places=2, max_digits=14)),
                ('precio_un_ta', models.DecimalField(decimal_places=2, help_text='Precio unitario temporada alta', max_digits=14)),
                ('precio_un_tb', models.DecimalField(decimal_places=2, help_text='Precio unitario temporada baja', max_digits=14)),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='ppl.planta')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='marketplace.producto')),
                ('socio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='marketplace.persona')),
            ],
            options={
                'unique_together': {('planta', 'socio', 'producto')},
            },
        ),
    ]