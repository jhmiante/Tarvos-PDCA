from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib import messages

from .forms import IncluirPdcaForm
from .functions import buscarDadosId, buscarDados


class AddPdcaView(FormView):
    template_name = 'pdca/pdca-additem.html'
    form_class = IncluirPdcaForm
    success_url = reverse_lazy('pdca-add')

    def get_context_data(self, **kwargs):
        context = super(AddPdcaView, self).get_context_data(**kwargs)
        user = self.request.user

        return context

    def form_valid(self, form, *args, **kwargs):
        form.cadastrar(self.request)
        messages.success(self.request, 'Cadastro realizado com sucesso!!!')
        return super(AddPdcaView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao cadastrar!!!')
        return super(AddPdcaView, self).form_invalid(form, *args, **kwargs)


class PDCAitem(TemplateView):
    template_name = 'pdca/pdca-item.html'

    def get_context_data(self, **kwargs):
        context = super(PDCAitem, self).get_context_data(**kwargs)
        context['pdca'] = buscarDados(self.request.user, False)

        return context



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