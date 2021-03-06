# Generated by Django 2.2.7 on 2019-12-04 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RazaMascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raza_mascota', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomb_mascota', models.CharField(max_length=200)),
                ('genero_mascota', models.CharField(choices=[('MACHO', 'Macho'), ('HEMBRA', 'Hembra')], default='MACHO', max_length=10)),
                ('propietario_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario')),
                ('raza_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.RazaMascota')),
                ('tip_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Tipomascota')),
            ],
        ),
    ]
