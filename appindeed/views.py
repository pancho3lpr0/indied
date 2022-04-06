from django.shortcuts import render, redirect
from .models import empleo, empresa, comentarios
from .forms import comentariosForm, userForm, loginForm
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView

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

class Registro(View):
  form_class = userForm
  initial = {'key': 'value'}
  template_name = 'app/pages/registro.html'

  def get (self, request, *args, **kwargs):
    form = self.form_class(initial=self.initial)
    return render(request, self.template_name, {'form': form})

  def post (self, request, *args, **kwargs):
    form = self.form_class(request.POST)
    if form.is_valid ():
        form.save ()
        username = form.cleaned_data.get ('username')
        messages.success (request, f'Account created for {username}')
        return redirect (to='/')
    return render (request, self.template_name, {'form': form})
  def dispatch (self, request, *args, **kwargs):
    # will redirect to the home page if a user tries to access the register page while logged in
    if request.user.is_authenticated:
        return redirect (to='/')
    # else process dispatch as it otherwise normally would
    return super (Registro, self).dispatch(request, *args, **kwargs)

class CustomLoginView(LoginView) :
 form_class = loginForm
 def form_valid (self, form) :
    remember_me = form.cleaned_data.get ('remember_me')
    if not remember_me:
        # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
        self.request.session.set_expiry(0)
        # Set session as modified to force data updates/cookie to be saved.
        self.request.session.modified = True
    # else browser session will be as long as the session cookie time "SESSION COOKIE AGE" defined in settings.py
    return super (CustomLoginView, self).form_valid(form)