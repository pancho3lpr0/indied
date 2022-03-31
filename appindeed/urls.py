from django.urls import path, include
from .views import index, imagenes, base, empresas, precios, funcionalidades, buscar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('imagenes/', imagenes, name='imagenes'),
    path('base/', base, name='base'),
    path('empresas/', empresas, name='empresas'),
    path('funcionalidades/', funcionalidades, name='funcionalidades'),    
    path('precios/', precios, name='precios'),
    path('buscar/', buscar, name='buscar')
]

urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

