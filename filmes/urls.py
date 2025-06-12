from django.urls import path
from filmes import views

urlpatterns = [
    path('cadastrar/', views.cadastrarFilme, name='cadastrarfilme'),
    path('listar/', views.listarFilmes, name='listarfilmes'),
    path('filmes/', views.filmes, name='filmes'),
    path('filmespagina/', views.filmespagina, name='filmespagina'),
    path('filmes/<int:foto_id>', views.filmes, name='filmes'),
    path('filmesdetalhes/', views.filmesdetalhes, name='filmesdetalhes'),
    path('filmesdetalhes2/', views.filmesdetalhes2, name='filmesdetalhes2'),
    path('filmesdetalhes3/', views.filmesdetalhes3, name='filmesdetalhes3'),
    path('filmesdetalhes4/', views.filmesdetalhes4, name='filmesdetalhes4'),
    # path('buscar', views.buscar, name='buscar'),
    # path('detalhes/', views.detalhes, name='detalhes'),
]


