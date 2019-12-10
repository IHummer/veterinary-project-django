# Generated by Django 3.0 on 2019-12-10 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20191210_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='estado',
            field=models.CharField(choices=[('DISPONIBLE', 'Listo para ser vendido'), ('AGOTADO', 'Producto agotado'), ('BAJO_STOCK', 'Bajo stock del producto')], default='DISPONIBLE', max_length=20),
        ),
    ]