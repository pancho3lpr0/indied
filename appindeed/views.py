from django.shortcuts import render
from .models import empleo, empresa, comentarios
from .forms import comentariosForm

# Create your views here.
def imagenes(request):
    return render(request, 'app/imagenes.html')

def base(request):
    return render(request, 'app/base.html')

def empresas(request):
    empresas = empresa.objects.all()
    datos = {
        "empresas" : empresas
    }
    return render(request, 'app/empresas.html', datos)

def index(request):
    datos = {
        "form": comentariosForm
    }
    
    if request.method == 'POST':
        formulario = comentariosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            datos["form"] = formulario
    return render(request, 'app/index.html', datos)

def precios(request):
    return render(request, 'app/precios.html')

def funcionalidades(request):
    empleos = empleo.objects.all()
    datos = {
        "empleos" : empleos
    }
    return render(request, 'app/funcionalidades.html', datos)

def buscar(request):
    if request.GET['busqueda']:
        query = request.GET['busqueda']
        empleos = empleo.objects.filter(titulo__icontains=query).order_by('-ubicacion')
        datos = {
            "empleos" : empleos,
            "query" : query
        }
        return render(request, 'app/buscar.html', datos)
    else:
        return render(request, 'app/buscar.html')