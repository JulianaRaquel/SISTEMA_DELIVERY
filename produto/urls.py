from django.urls import path
from .views import home, categoria, produto, add_carrinho, ver_carrinho, remover_carrinho

urlpatterns = [
    path('', home, name='home'),
    path('categoria/<int:id>', categoria, name='categoria'),
    path('produto/<int:id>', produto, name='produto'),
    path('add_carrinho/', add_carrinho, name='add_carrinho'),
    path('ver_carrinho/', ver_carrinho, name="ver_carrinho"),
    path('remover_carrinho/<int:id>', remover_carrinho, name="remover_carrinho"),
]
