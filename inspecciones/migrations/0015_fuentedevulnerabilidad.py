# Generated by Django 5.0.4 on 2024-05-02 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspecciones', '0014_remove_inspeccion_equipo_inspeccion_componente'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuenteDeVulnerabilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
