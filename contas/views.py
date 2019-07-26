from django.shortcuts import render
from .models import Pessoa

# Create your views here.
def mostrar_formulario_cadastro(request):
    contexto = {'msg': None}
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.cpf = request.POST.get('cpf')
        pessoa.email = request.POST.get('email')
        pessoa.telefone = request.POST.get('telefone')
        pessoa.genero = request.POST.get('genero')
        pessoa.save()
        contexto = {'msg': 'ae parabéns'}
    return render(request, 'index.html', contexto)

def mostrar_pessoas(request):
    pessoas = Pessoa.objects.all()

    return render(request, 'pessoas.html', {'dados': pessoas})