# Generated by Django 4.1.6 on 2024-04-22 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspecciones', '0007_remove_inspeccion_fotos_foto_inspeccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='imagen',
            field=models.ImageField(upload_to=''),
        ),
    ]
