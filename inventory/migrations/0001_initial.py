# Generated by Django 2.2.7 on 2019-11-23 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_nomb', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca_nomb', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tipomascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip_mascota', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_nomb', models.CharField(max_length=150)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('estado', models.CharField(choices=[('DISPONIBLE', 'Listo para ser vendido'), ('AGOTADO', 'Producto agotado'), ('REABASTECIENDO', 'Reabastecimiento en proceso')], default='DISPONIBLE', max_length=20)),
                ('cat_prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Categoria')),
                ('marca_nomb', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Marca')),
                ('tip_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Tipomascota')),
            ],
        ),
    ]
