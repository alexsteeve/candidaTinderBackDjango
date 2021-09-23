from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from CandidaTinderApp.models import Partidos, Propostas, Usuarios, Parlamentares, VotacoesParlamentares, VotacoesUsuarios
from CandidaTinderApp.serializer import PartidosSerializer, PropostasSerializer, UsuariosSerializer, ParlamentaresSerializer, VotacoesParlamentaresSerializer, VotacoesUsuariosSerializer

# Create your views here.
@csrf_exempt
def partidosApi(request,id=0):
    if request.method=='GET':
        partidos = Partidos.objects.all()
        partidos_serializer = PartidosSerializer(partidos, many=True)
        return JsonResponse(partidos_serializer.data, safe=False)

    elif request.method=='POST':
        partidos_data = JSONParser().parse(request)
        partidos_serializer = PartidosSerializer(data=partidos_data)
        if partidos_serializer.is_valid():
            partidos_serializer.save()
            return JsonResponse("Partido incluído com sucesso!", safe=False)
        return JsonResponse("Falha ao incluir um partido.", safe=False)

    elif request.method=='PUT':
        partidos_data = JSONParser().parse(request)
        partidos=Partidos.objects.get(IdPartido=partidos_data['IdPartido'])
        partidos_serializer=PartidosSerializer(partidos,data=partidos_data)
        if partidos_serializer.is_valid():
            partidos_serializer.save()
            return JsonResponse("Partido atualizado com sucesso!", safe=False)
        return JsonResponse("Falha ao atualizar um partido.", safe=False)

    elif request.method=='DELETE':
        partidos = Partidos.objects.get(IdPartido=id)
        partidos.delete()
        return JsonResponse("Partido apagado com sucesso!", safe=False) 

@csrf_exempt
def propostasApi(request,id=0):
    if request.method=='GET':
        propostas = Propostas.objects.all()
        propostas_serializer = PropostasSerializer(propostas, many=True)
        return JsonResponse(propostas_serializer.data, safe=False)

    elif request.method=='POST':
        propostas_data = JSONParser().parse(request)
        propostas_serializer = PropostasSerializer(data=propostas_data)
        if propostas_serializer.is_valid():
            propostas_serializer.save()
            return JsonResponse("Proposta incluída com sucesso!", safe=False)
        return JsonResponse("Falha ao incluir uma proposta.", safe=False)

    elif request.method=='PUT':
        propostas_data = JSONParser().parse(request)
        propostas=Propostas.objects.get(IdProposta=propostas_data['IdProposta'])
        propostas_serializer=PropostasSerializer(propostas,data=propostas_data)
        if propostas_serializer.is_valid():
            propostas_serializer.save()
            return JsonResponse("Proposta atualizada com sucesso!", safe=False)
        return JsonResponse("Falha ao atualizar uma proposta.", safe=False)

    elif request.method=='DELETE':
        propostas = Propostas.objects.get(IdProposta=id)
        propostas.delete()
        return JsonResponse("Proposta apagada com sucesso!", safe=False) 

@csrf_exempt
def usuariosApi(request,id=0):
    if request.method=='GET':
        usuarios = Usuarios.objects.all()
        usuarios_serializer = UsuariosSerializer(usuarios, many=True)
        return JsonResponse(usuarios_serializer.data, safe=False)

    elif request.method=='POST':
        usuarios_data = JSONParser().parse(request)
        usuarios_serializer = UsuariosSerializer(data=usuarios_data)
        if usuarios_serializer.is_valid():
            usuarios_serializer.save()
            return JsonResponse("Usuario incluido com sucesso!", safe=False)
        return JsonResponse("Falha ao incluir um usuario.", safe=False)

    elif request.method=='PUT':
        usuarios_data = JSONParser().parse(request)
        usuarios=Usuarios.objects.get(IdUsuario=usuarios_data['IdUsuario'])
        usuarios_serializer=UsuariosSerializer(usuarios,data=usuarios_data)
        if usuarios_serializer.is_valid():
            usuarios_serializer.save()
            return JsonResponse("Usuario atualizado com sucesso!", safe=False)
        return JsonResponse("Falha ao atualizar um usuario.", safe=False)

    elif request.method=='DELETE':
        usuarios = Usuarios.objects.get(IdUsuario=id)
        usuarios.delete()
        return JsonResponse("Usuario apagado com sucesso!", safe=False) 

@csrf_exempt
def parlamentaresApi(request,id=0):
    if request.method=='GET':
        parlamentares = Parlamentares.objects.all()
        parlamentares_serializer = ParlamentaresSerializer(parlamentares, many=True)
        return JsonResponse(parlamentares_serializer.data, safe=False)

    elif request.method=='POST':
        parlamentares_data = JSONParser().parse(request)
        parlamentares_serializer = ParlamentaresSerializer(data=parlamentares_data)
        if parlamentares_serializer.is_valid():
            parlamentares_serializer.save()
            return JsonResponse("Parlamentar incluido com sucesso!", safe=False)
        return JsonResponse("Falha ao incluir um parlamentar.", safe=False)

    elif request.method=='PUT':
        parlamentares_data = JSONParser().parse(request)
        parlamentares=Parlamentares.objects.get(IdParlamentar=parlamentares_data['IdParlamentar'])
        parlamentares_serializer=ParlamentaresSerializer(parlamentares,data=parlamentares_data)
        if parlamentares_serializer.is_valid():
            parlamentares_serializer.save()
            return JsonResponse("Parlamentar atualizado com sucesso!", safe=False)
        return JsonResponse("Falha ao atualizar um parlamentar.", safe=False)

    elif request.method=='DELETE':
        parlamentares = Parlamentares.objects.get(IdParlamentar=id)
        parlamentares.delete()
        return JsonResponse("Parlamentar apagado com sucesso!", safe=False) 

@csrf_exempt
def votacoesParlamentaresApi(request,id=0):
    if request.method=='GET':
        votacoesParlamentares = VotacoesParlamentares.objects.all()
        votacoesParlamentares_serializer = VotacoesParlamentaresSerializer(votacoesParlamentares, many=True)
        return JsonResponse(votacoesParlamentares_serializer.data, safe=False)

    elif request.method=='POST':
        votacoesParlamentares_data = JSONParser().parse(request)
        votacoesParlamentares_serializer = VotacoesParlamentaresSerializer(data=votacoesParlamentares_data)
        if votacoesParlamentares_serializer.is_valid():
            votacoesParlamentares_serializer.save()
            return JsonResponse("Votacao do parlamentar incluida com sucesso!", safe=False)
        return JsonResponse("Falha ao incluir uma votacao de parlamentar.", safe=False)

    elif request.method=='PUT':
        votacoesParlamentares_data = JSONParser().parse(request)
        votacoesParlamentares=VotacoesParlamentares.objects.get(IdVotacao=votacoesParlamentares_data['IdVotacao'])
        votacoesParlamentares_serializer=VotacoesParlamentaresSerializer(votacoesParlamentares,data=votacoesParlamentares_data)
        if votacoesParlamentares_serializer.is_valid():
            votacoesParlamentares_serializer.save()
            return JsonResponse("Votacao do parlamentar atualizada com sucesso!", safe=False)
        return JsonResponse("Falha ao atualizar uma votacao de parlamentar.", safe=False)

    elif request.method=='DELETE':
        votacoesParlamentares = VotacoesParlamentares.objects.get(IdVotacao=id)
        votacoesParlamentares.delete()
        return JsonResponse("Votacao de parlamentar apagada com sucesso!", safe=False) 

@csrf_exempt
def VotacoesUsuariosApi(request,id=0):
    if request.method=='GET':
        votaCoesUsuarios = VotacoesUsuarios.objects.all()
        votacoesUsuarios_serializer = VotacoesUsuariosSerializer(votaCoesUsuarios, many=True)
        return JsonResponse(votacoesUsuarios_serializer.data, safe=False)

    elif request.method=='POST':
        votacoesUsuarios_data = JSONParser().parse(request)
        votacoesUsuarios_serializer = VotacoesUsuariosSerializer(data=votacoesUsuarios_data)
        if votacoesUsuarios_serializer.is_valid():
            votacoesUsuarios_serializer.save()
            return JsonResponse("Votacao do usuario incluida com sucesso!", safe=False)
        return JsonResponse("Falha ao incluir uma votacao de usuario.", safe=False)

    elif request.method=='PUT':
        votacoesUsuarios_data = JSONParser().parse(request)
        votacoesUsuarios=VotacoesUsuarios.objects.get(IdVotacao=votacoesUsuarios_data['IdVotacao'])
        votacoesUsuarios_serializer=VotacoesUsuariosSerializer(votacoesUsuarios,data=votacoesUsuarios_data)
        if votacoesUsuarios_serializer.is_valid():
            votacoesUsuarios_serializer.save()
            return JsonResponse("Votacao do usuario atualizada com sucesso!", safe=False)
        return JsonResponse("Falha ao atualizar uma votacao de usuario.", safe=False)

    elif request.method=='DELETE':
        votacoesUsuarios = VotacoesUsuarios.objects.get(IdVotacao=id)
        votacoesUsuarios.delete()
        return JsonResponse("Votacao de usuario apagada com sucesso!", safe=False) 

