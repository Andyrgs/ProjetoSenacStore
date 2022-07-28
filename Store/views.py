from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from Store.models import Categoria, Departamento, Categoria, Produto
from Store.models import Produto
# Create your views here.
def index(request):
    meu_nome = 'Andy da Silva'
    sexo = 'M'
    context = {'nome': meu_nome,'artigo':'o' if sexo == 'M' else 'a'}
    return render(request,'index.html', context)

def departamentos(request):
  #  depto = ['Casa','Informatica','Telefonia']
    depto = Departamento.objects.all()
    context = {'departamentos': depto}
    return render(request,'departamentos.html', context)

def categorias(request):
     listas_categorias = Categoria.objects.all()
     context = {'categorias': listas_categorias}
     return render(request,'categorias.html', context)

def produtos(request):
     listas_produtos = produtos.objects.all()
     context = {'produtos': listas_produtos}
     return render(request,'produtos.html', context)