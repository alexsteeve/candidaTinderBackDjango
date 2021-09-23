from django.conf.urls import url
from CandidaTinderApp import views

urlpatterns=[
    url(r'^partidos/$',views.partidosApi),
    url(r'^partidos/([0-9]+)$',views.partidosApi),
    url(r'^propostas/$',views.propostasApi),
    url(r'^propostas/([0-9]+)$',views.propostasApi),
    url(r'^usuarios/$',views.usuariosApi),
    url(r'^usuarios/([0-9]+)$',views.usuariosApi),
    url(r'^parlamentares/$',views.parlamentaresApi),
    url(r'^parlamentares/([0-9]+)$',views.parlamentaresApi),
    url(r'^votacaoparlamentares/$',views.votacoesParlamentaresApi),
    url(r'^votacaoparlamentares/([0-9]+)$',views.votacoesParlamentaresApi),
    url(r'^votacaousuarios/$',views.VotacoesUsuariosApi),
    url(r'^votacaousuarios/([0-9]+)$',views.VotacoesUsuariosApi)
]