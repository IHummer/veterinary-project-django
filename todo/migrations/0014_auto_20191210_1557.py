# Generated by Django 3.0 on 2019-12-10 15:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0013_auto_20191210_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=django.utils.timezone.now, unique=True),
            preserve_default=False,
        ),
    ]
