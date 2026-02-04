from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models. CharField(max_length=16)
    email = models.EmailField()
    cep = models.CharField(max_length=9)
    numero = models. IntegerField()
    compl = models.CharField(max_length=20)

    def _str_ (self) :
        return self.nome