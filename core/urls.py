from django.urls import path
from .views import cliente_novo, index, viewImoveis


urlpatterns = [
    path('', index, name='index'),
    path("view_imoveis/<int:ID_Imovel>/", viewImoveis, name="view_imoveis"),
    path('cliente_novo/', cliente_novo, name='cliente_novo'),
]
