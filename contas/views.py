from django.shortcuts import render
from .models import Pessoa

# Create your views here.
def mostrar_formulario_cadastro(request):
    pessoa = Pessoa(request.POST)
    pessoa.save()
    
    return render(request, 'index.html')

