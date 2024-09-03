from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from . import models

class ListaProdutos(ListView):
        model = models.Produto
        template_name = 'produto/list.html'

class DetalheProduto(View):
    pass

class AdicionarAoCarrinho(View):
    pass

class RemoverDoCarrinho(View):
    pass

class Carrinho(View):
    pass

class Finalizar(View):
    pass