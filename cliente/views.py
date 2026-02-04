from django.http import HttpResponse
from django.shortcuts import render

import requests

from cliente.models import Cliente


def busca_cep(requests):
    endereco = {}


def cadastrar_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        cep = request.POST.get('cep')
        numero = request.POST.get('numero')
        compl = request.POST.get('compl')

        if nome and telefone and email and cep and numero and compl:

            cliente = Cliente(nome=nome, telefone=telefone, email=email, numero=numero, compl=compl)

            cliente.save()

            return HttpResponse(
                f"Cliente cadastrado com sucesso! <br> "
                f"Nome: {cliente.nome}"
                f"<br> Telefone: {cliente.telefone}"
                 f"<br>Email: {cliente.email}"
            )
    return render(request, 'cadastro_cliente.html')

