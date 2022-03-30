from django.contrib import admin
from .models import empleo, empresa, comentarios

# Register your models here.
class Jobs(admin.ModelAdmin):
    list_display = ["titulo","descripcion_corta","salario_tiempo"]
    list_editable = ["salario_tiempo"]
    search_fields = ["titulo","descripcion_corta"]
    list_filter = ["salario_tiempo"]
    list_per_page = 10

class Business(admin.ModelAdmin):
    list_display = ["empleos","salarios","title_business","imagen"]
    list_editable = ["title_business"]
    search_fields = ["title_business","empleos"]
    list_filter = ["salarios"]
    list_per_page = 10

admin.site.register(empleo, Jobs)
admin.site.register(empresa, Business)
admin.site.register(comentarios)