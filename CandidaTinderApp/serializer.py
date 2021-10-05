from rest_framework import serializers
from CandidaTinderApp.models import CandidatoUsuario, Parlamentares, PartidoUsuario, Partidos, Propostas, Usuarios, VotacoesParlamentares, VotacoesUsuarios

class PartidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partidos
        fields = ('IdPartido',
                    'SiglaPartido',
                    'NomePartido')

class PropostasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propostas
        fields = ('IdProposta',
                    'CodigoProposta',
                    'DataProposta',
                    'Link1Proposta',
                    'Link2Proposta',
                    'Popularidade',
                    'NomeProposta')

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Usuarios
        fields = ('IdUsuario',
                    'Login',
                    'Senha',
                    'Nome',
                    'Estado',
                    'Idade'
                    )

class ParlamentaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parlamentares
        fields = ('IdParlamentar',
            'NomeParlamentar',
            'IdPartido',
            'EstadoParlamentar',
            'IdParlamentarEleito')

class VotacoesParlamentaresSerializer(serializers.ModelSerializer):
    class Meta: 
        model = VotacoesParlamentares
        fields = ('IdVotacao',
                    'IdParlamentar',
                    'IdProposta',
                    'Voto')

class VotacoesUsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = VotacoesUsuarios
        fields = ('IdVotacao',
                    'IdUsuario',
                    'IdProposta',
                    'Voto')

class CandidatoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidatoUsuario
        fields = ('IdCandidatoUsuario',
                    'IdUsuario',
                    'OrdemAfinidade',
                    'IdParlamentar',
                    'PercentualParlamentar')

class PartidoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartidoUsuario
        fields = ('IdPartidoUsuario',
                    'IdUsuario',
                    'OrdemAfinidade',
                    'IdPartido',
                    'PercentualPartido')