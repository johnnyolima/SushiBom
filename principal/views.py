from django.shortcuts import render, get_object_or_404
from categoria.models import Categoria
from produto.models import Produto


def inicio(request):
    return render(request, 'home.html')


def historia(request):
    return render(request, 'historia.html')


def sushi(request):
    sushi = Categoria.objects.get(nome='sushi')
    produtos = Produto.objects.filter(categoria=sushi)
    return render(request, "sushi.html",{'produtos': produtos})

def temaki(request):
    temaki = Categoria.objects.get(nome='temaki')
    produtos = Produto.objects.filter(categoria=temaki)
    return render(request, "temaki.html",{'produtos': produtos})

def bebidas(request):
    bebidas = Categoria.objects.get(nome='bebidas')
    produtos = Produto.objects.filter(categoria=bebidas)
    return render(request, "bebidas.html",{'produtos': produtos})

def sobremesas(request):
    sobremesas = Categoria.objects.get(nome='sobremesas')
    produtos = Produto.objects.filter(categoria=sobremesas)
    return render(request, "sobremesas.html",{'produtos': produtos})


def outros(request):
    outros = Categoria.objects.get(nome='outros')
    produtos = Produto.objects.filter(categoria=outros)
    return render(request, "outros.html",{'produtos': produtos})


def administrativo(request):
    return render(request, 'menuadm.html')
