# Generated by Django 4.0.1 on 2022-03-23 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appindeed', '0008_comentarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='comentario',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='nombre',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
