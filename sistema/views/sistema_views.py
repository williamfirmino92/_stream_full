from django.shortcuts import render

from sistema.models import Filme

# Aqui irão ficar todas as views (controladores) ref ao App sistema
# A função index informa o que vai acontecer quando ela for chamada.

def index(request):
    filmes = Filme.objects.order_by('data_cadastro').filter(publicado=True)
    return render(
        request,
        'sistema/index.html',
        {"cards": filmes}
    )



def suporte(request):
    return render(
        request,
        'sistema/suporte.html',
    )



# Função atual
# def index(request):
#     return render(
#         request,
#         'sistema/index.html',
#     )