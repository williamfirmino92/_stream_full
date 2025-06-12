from django.shortcuts import get_object_or_404, render, redirect
from sistema.models import Filme
from filmes.forms import FilmeForm

def cadastrarFilme(request):

    if request.method == "POST":
        form = FilmeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()   
            return redirect('listar')
    else:
        form = FilmeForm()

    return render(
        request,
        'filmes/cadastrar.html',
        {'form': form},
    )

def listarFilmes(request):
    filmes = Filme.objects.all()
    
    context = {
        'filmes': filmes,
    }
    
    return render(
        request,
        'filmes/listar.html',
        context,
    )

# View ref ao detalhes do filme
def filmes(request, filme_id):
    filme = get_object_or_404(Filme, pk=filme_id)
    return render(
        request,
        "filmes/filme_detalhe.html",
        {"filme": filme}
    )
    
def filmesdetalhes(request):
    return render(
        request,
        'filmes/filmes_detalhes_premonicao.html',
    )

# view ref a opção de buscar filmes:
# def buscar(request):
#     filmes = Filme.objects.order_by('data_cadastro').filter(publicada=True)

#     if "buscar" in request.GET:
#         nome_a_buscar = request.GET['buscar']
#         if nome_a_buscar:
#             filmes = filmes.filter(nome__icontains=nome_a_buscar)
#     return render (
#         request, 'filmes/buscar.html', {"cards": filmes}
#     )



# def detalhes(request):
#     return render(
#         request,
#         'filmes/filme_detalhe.html',
#     )

# def filmes(request):
#     return render(
#         request,
#         'filmes/filmes.html',
#     )