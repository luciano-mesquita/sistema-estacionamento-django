from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista-pessoas/', views.lista_pessoas, name='est_lista_pessoas'),
    path('lista-veiculos/', views.lista_veiculos, name='est_lista_veiculos'),
    path('lista-rotativos/', views.lista_rotativos, name='est_lista_rotativos'),

    path('cadastra-pessoa/', views.cadastra_pessoa, name='est_cadastra_pessoa'),
    path('cadastra-veiculo/', views.cadastra_veiculo, name='est_cadastra_veiculo'),
    path('cadastra-rotativo/', views.cadastra_rotativo, name='est_cadastra_rotativo'),

    path('atualiza-pessoa/<int:id>/', views.atualiza_pessoa, name='est_atualiza_pessoa'),
    path('atualiza-veiculo/<int:id>/', views.atualiza_veiculo, name='est_atualiza_veiculo'),
    path('atualiza-rotativo/<int:id>/', views.atualiza_rotativo, name='est_atualiza_rotativo'),

    path('deleta-pessoa/<int:id>/', views.deleta_pessoa, name='est_deleta_pessoa'),
    path('deleta-veiculo/<int:id>/', views.deleta_veiculo, name='est_deleta_veiculo'),
    path('deleta-rotativo/<int:id>', views.deleta_rotativo, name='est_deleta_rotativo'),
]