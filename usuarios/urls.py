from django.urls import path
from . import views

urlpatterns = [
    #primeiro parametro -> rota
    #segundo parametro -> qual view?
    #terceiro parametro -> identificador esclusivo
    #(para ser usado em pesquisa reservada)
    path('', views.home, name="home"),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    #path('usuarios/<int:id>/', views.buscar_usuarios)
    #path('usuarios/', views.listar_usuarios_co)
]