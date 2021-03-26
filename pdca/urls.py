from django.urls import path
from django.views.generic.base import TemplateView


from . import views as view

urlpatterns = [
    path('pdca/', view.PDCA, name='pdca'),
    path('pdca/add', view.AddPdcaView.as_view(), name='pdca-add'),
    path('pdca/item', view.PDCAitem.as_view(), name='pdca-item'),
    path('pdca/finalizados', view.PDCAfinalizados, name='pdca-finalizados')
]
