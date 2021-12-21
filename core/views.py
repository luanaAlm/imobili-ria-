from django.shortcuts import render
from core.form import ImovelForm, ClienteForm
from core.models import Depoimento, Imovel
# from .form import ClienteForm
from django.shortcuts import redirect, render


def index(request):
    destaques = Imovel.objects.filter(categoria="Destaque")
    casas = Imovel.objects.filter(categoria="Casa")
    apartamentos = Imovel.objects.filter(categoria="Apartamento")
    depoimento = Depoimento.objects.all()

    form = ClienteForm()

    return render(request, "index.html", {
        "destaques": destaques,
        "casas": casas,
        "apartamentos": apartamentos,
        "depoimento": depoimento,
        "form": form
    })


def viewImoveis(request, ID_Imovel):
    data = {}
    imoveis = Imovel.objects.get(ID_Imovel=ID_Imovel)
    form = ImovelForm(request.POST or None, instance=imoveis)
    data["imoveis"] = imoveis
    data["form"] = form
    return render(request, "view_imoveis.html", data)


def cliente_novo(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        # messages.success(request, 'Sua mensagem foi enviada com sucesso!')
        return redirect('index')
    else:
        # messages.error(
        #     request, 'Houve um erro, reenvie novamente a mensagem!')
        return redirect('index')
