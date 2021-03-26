from django.urls import path
from django.views.generic.base import TemplateView


from . import views as vw
from . import classViews as cw

urlpatterns = [
    path('pdca/', vw.PDCA, name='pdca'),
    path('pdca/add', cw.AddPdcaView.as_view(), name='pdca-add'),
    path('pdca/item', cw.PDCAitem.as_view(), name='pdca-item'),
    path('pdca/finalizados', vw.PDCAfinalizados, name='pdca-finalizados')
]
