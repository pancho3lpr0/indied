from django.db import models
#import datetime

# Create your models here.
class empleo(models.Model):
    descripcion_corta = models.CharField(max_length=300, blank=False , null=False)
    titulo = models.CharField(max_length=50, blank=False, null=False)
    links = models.URLField(blank=True, null=True)
    ubicacion = models.CharField(max_length=50, blank=True, null=True)
    salario_tiempo = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    def __str__(self):
        return self.titulo

class empresa(models.Model) :
    banner = models.ImageField(blank = True, null=True, upload_to='imagenes')
    imagen = models.ImageField(blank = True, null=True, upload_to='imagenes')
    title_business = models.CharField(blank=False, null=False, max_length=100)
    empleos = models.TextField(blank=False, null=False)
    salarios = models.TextField(blank=False, null=False)
    def __str__(self):
        return self.title_business

class comentarios(models.Model) :
    nombre = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    comentario = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.nombre