from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib import messages

from .forms import IncluirPdcaForm
from .functions import buscarDadosId, buscarDados
from .models import PDCA


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

