from multiprocessing import context
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


def categorias(request, id):
     listas_categorias = Categoria.objects.filter(departamento_id = id)
     depto = Departamento.objects.get(id=id)
     context = {
            'categorias': listas_categorias,
            'departamento': depto
            }
     return render(request,'categorias.html', context)


def produtos(request, id):
     listas_produtos = Produto.objects.filter(categoria_id = id)
     context = {'produtos': listas_produtos}
     return render(request,'produtos.html', context)

def produto_detalhe(request, id):
    produto = produtos.objects.get(id = id)
    context = {
                'produto': produto
    }
    return render(request,'produto_detalhe.html',context)

def institucional (request):
    return render(request, 'institucional.html')    

def contato(resquest):
  return render(request, 'contato.html')   