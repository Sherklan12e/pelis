# Generated by Django 5.0.4 on 2024-04-19 22:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_alter_pelicula_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('portada', models.CharField(max_length=250)),
                ('descripcion', models.TextField()),
                ('fecha_estreno_serie', models.DateField()),
                ('duracion', models.PositiveBigIntegerField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AlterModelOptions(
            name='pelicula',
            options={'ordering': ['-id']},
        ),
        migrations.CreateModel(
            name='agregar_cap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=240)),
                ('fecha', models.DateField()),
                ('codigo_serie', models.TextField()),
                ('seriea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partesss', to='login.series')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]