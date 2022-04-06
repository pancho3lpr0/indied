from django import forms
from .models import empleo,empresa,comentarios
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class comentariosForm(forms.ModelForm):
    class Meta:
        model = comentarios
        fields = ["nombre", "email", "comentario"]
        #fields = '__all__'
    
class userForm(UserCreationForm) :
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class loginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']
    user_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(max_length=50, required=True, widget=forms.forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'data-toggle': 'password', 'id': 'password', 'name': 'password'}))
    remember_me = forms.BooleanField(required=False)
    