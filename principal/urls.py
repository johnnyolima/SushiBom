from django.urls import path
from . import views
from .views import historia, sushi, temaki, sobremesas, bebidas, administrativo, outros, inicio

urlpatterns = [
    path('', inicio, name='inicio'),
    path('historia/', historia, name='historia'),
    path('sushi/', sushi, name='sushi'),
    path('temaki/', temaki, name='temaki'),
    path('sobremesas/', sobremesas, name='sobremesas'),
    path('bebidas/', bebidas, name='bebidas'),
    path('administrativo/', administrativo, name='administrativo'),
    path('outros/', outros, name='outros'),
]
