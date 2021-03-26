from django.shortcuts import render
from django.contrib import messages


from .forms import IncluirPdcaForm
from .functions import AddPDCA, buscarDadosId, buscarDados
from .models import PDCA


def PDCA(request):
    return render(request, 'pdca/pdca-index.html')


def PDCAfinalizados(request):

    if str(request.method) == 'POST':
        final = request.POST.get("finalizar")
        pdca = buscarDadosId(final)
        pdca.finalizado = True
        pdca.save()

        listPdca = buscarDados(request.user, True)
    else:
        listPdca = buscarDados(request.user, True)

    print(listPdca)

    context = {
        'pdca': listPdca
    }

    return render(request, 'pdca/pdca-finalizados.html', context)


"""
def AddItem(request):
    form = IncluirPdcaForm(request.POST or None)

    if str(request.method) == 'POST':

        if form.is_valid():
            objetivo = form.cleaned_data['objetivo']
            inicio = form.cleaned_data['inicio']
            fim = form.cleaned_data['fim']
            quem = form.cleaned_data['quem']
            descricao = form.cleaned_data['descricao']

            print(request.user, objetivo, inicio, fim, quem, descricao)

            AddPDCA(request.user, objetivo, inicio, fim, quem, descricao)

            messages.success(request, 'PDCA Criado com Sucesso')
            form = IncluirPdcaForm()
        else:
            messages.error(request, 'Erro ao cadastrar PDCA')

    context = {
        'form': form
    }

    return render(request, 'pdca/pdca-additem.html', context)
"""