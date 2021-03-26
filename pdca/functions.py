from .models import PDCA
from datetime import date


def AddPDCA(usuario, objetivo, inicio, fim, quem, descricao):
    pdca = PDCA(
        usuario=usuario,
        objetivo=objetivo,
        data=date.today(),
        inicio=inicio,
        fim=fim,
        quem=quem,
        descricao=descricao
    )
    pdca.save()


def buscarDadosId(id):
    return PDCA.objects.get(id=id)


def buscarDados(usuario, status):
    if usuario.is_adm:
        return PDCA.objects.filter(
            finalizado=status,
            usuario__empresa=usuario.empresa
        )
    else:
        return PDCA.objects.filter(
            finalizado=status,
            usuario=usuario
        )
