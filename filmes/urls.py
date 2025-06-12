from django.urls import path
from filmes import views

urlpatterns = [
    path('cadastrar/', views.cadastrarFilme, name='cadastrarfilme'),
    path('listar/', views.listarFilmes, name='listarfilmes'),
    path('filmes/', views.filmes, name='filmes'),
    path('filmes/<int:foto_id>', views.filmes, name='filmes'),
    # path('buscar', views.buscar, name='buscar'),
    # path('detalhes/', views.detalhes, name='detalhes'),
]


