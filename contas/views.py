from django.shortcuts import render
from .models import Pessoa

# Create your views here.
def mostrar_formulario_cadastro(request):
    if request.method == 'POST':       
        pessoa = Pessoa()
        pessoa.nome = request.POST['nome']
        pessoa.cpf = request.POST['cpf']
        pessoa.save()

    return render(request, 'index.html')

