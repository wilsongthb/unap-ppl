# Generated by Django 4.1.3 on 2023-01-17 00:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('imagen_ref', models.ImageField(blank=True, null=True, upload_to='categorias/images')),
                ('icon_ref', models.ImageField(blank=True, null=True, upload_to='categorias/icons')),
                ('visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ndep', models.CharField(max_length=2)),
                ('nprov', models.CharField(default='00', max_length=2)),
                ('ndist', models.CharField(default='00', max_length=2)),
                ('nlugar', models.CharField(default='00', max_length=2)),
                ('tipo', models.CharField(max_length=2)),
                ('nombre', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='MapMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=255)),
                ('icon_file', models.ImageField(blank=True, null=True, upload_to='map_markers/icons')),
                ('lat', models.DecimalField(decimal_places=10, max_digits=18)),
                ('lng', models.DecimalField(decimal_places=10, max_digits=18)),
                ('type', models.CharField(max_length=2)),
                ('instance_id', models.PositiveBigIntegerField(null=True)),
                ('visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=1)),
                ('dni', models.CharField(max_length=8, null=True)),
                ('ruc', models.CharField(max_length=11, null=True)),
                ('nombre_completo', models.CharField(max_length=255)),
                ('ap_paterno', models.CharField(max_length=50, null=True)),
                ('ap_materno', models.CharField(max_length=50, null=True)),
                ('nombres', models.CharField(max_length=200)),
                ('sexo', models.CharField(default='N', help_text='F: Femenino, M: Masculino, N: Ninguno', max_length=1)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('razon_social', models.CharField(max_length=255, null=True)),
                ('ndep', models.CharField(help_text='Codigo departamento', max_length=2, null=True)),
                ('nprov', models.CharField(help_text='Codigo Provincia', max_length=2, null=True)),
                ('ndist', models.CharField(help_text='Codigo Distrito', max_length=2, null=True)),
                ('direccion', models.CharField(max_length=150, null=True)),
                ('lat_ubi', models.DecimalField(decimal_places=10, help_text='Latitud de ubicacion', max_digits=18, null=True)),
                ('lng_ubi', models.DecimalField(decimal_places=10, help_text='Longitud de ubicacion', max_digits=18, null=True)),
                ('telefono1', models.CharField(max_length=30)),
                ('telefono2', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='personas/foto_perfil')),
                ('user_id', models.PositiveBigIntegerField(blank=True, help_text='Usuario vinculado a esta persona', null=True, unique=True)),
                ('visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=50)),
                ('imagen_ref', models.ImageField(blank=True, null=True, upload_to='productos/images')),
                ('es_base', models.BooleanField(default=False)),
                ('base_id', models.PositiveBigIntegerField(null=True)),
                ('es_materia_prima', models.BooleanField(default=False)),
                ('codigo', models.CharField(blank=True, max_length=30, null=True)),
                ('descripcion', models.CharField(max_length=255, null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=12)),
                ('visible', models.BooleanField(default=True)),
                ('creador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('simbolo', models.CharField(max_length=5, null=True)),
            ],
            options={
                'unique_together': {('nombre', 'simbolo')},
            },
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('precio_original', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('mostrar_pre_org', models.BooleanField(default=False, help_text='Mostrar precio original')),
                ('cantidad', models.DecimalField(decimal_places=2, default=1, help_text='Cantidad disponible', max_digits=14)),
                ('visible', models.BooleanField(default=True)),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('map_mark', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='marketplace.mapmark')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='marketplace.producto')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='unidad_medida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='marketplace.unidadmedida'),
        ),
        migrations.AddIndex(
            model_name='persona',
            index=models.Index(fields=['tipo', 'dni', 'ruc'], name='marketplace_tipo_44cbf3_idx'),
        ),
        migrations.AddIndex(
            model_name='persona',
            index=models.Index(fields=['nombres', 'ap_paterno', 'ap_materno', 'razon_social'], name='marketplace_nombres_224e21_idx'),
        ),
        migrations.AddIndex(
            model_name='persona',
            index=models.Index(fields=['ndep', 'nprov', 'ndist'], name='marketplace_ndep_337bdc_idx'),
        ),
        migrations.AddIndex(
            model_name='lugar',
            index=models.Index(fields=['ndep', 'nprov', 'ndist', 'nlugar', 'tipo'], name='marketplace_ndep_a5ca7c_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='lugar',
            unique_together={('ndep', 'nprov', 'ndist', 'nlugar', 'tipo')},
        ),
    ]
