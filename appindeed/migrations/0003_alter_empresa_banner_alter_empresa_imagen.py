# Generated by Django 4.0.1 on 2022-02-24 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appindeed', '0002_remove_empresa_evaluaciones_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]
