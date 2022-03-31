from cProfile import label
#from tkinter.tix import Form
from django import forms
from .models import empleo,empresa,comentarios

class comentariosForm(forms.ModelForm):
    class Meta:
        model = comentarios
        fields = ["nombre", "email", "comentario"]
        #fields = '__all__'
    
