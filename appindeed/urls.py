from django.urls import path, include
from .views import index, imagenes, base, empresas, precios, funcionalidades, buscar, Registro, CustomLoginView
from django.conf import settings
from django.conf.urls.static import static
from .forms import loginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('imagenes/', imagenes, name='imagenes'),
    path('base/', base, name='base'),
    path('empresas/', empresas, name='empresas'),
    path('funcionalidades/', funcionalidades, name='funcionalidades'),    
    path('precios/', precios, name='precios'),
    path('buscar/', buscar, name='buscar'),
    path('registro/', Registro.as_view(), name='registro'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='app/login.html', authentication_form=loginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app/logout.html'), name='logout'),
]

urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

