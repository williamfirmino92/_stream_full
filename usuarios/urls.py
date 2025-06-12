from django.urls import path
from usuarios import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('login/', views.login, name='login'),
    path('esqueci/', views.esqueci, name='esqueci'),
    path('logout/', views.logout, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
]
