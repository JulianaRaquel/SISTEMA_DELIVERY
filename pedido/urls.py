from django.urls import path
from .views import finalizar_pedido, validaCupom

urlpatterns = [
    path('finalizar_pedido/', finalizar_pedido, name="finalizar_pedido"),
    path("validaCupom/", validaCupom, name='validaCupom'),
]