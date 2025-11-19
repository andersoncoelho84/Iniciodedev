from django.shortcuts import render

from django.http import JsonResponse

from usuarios.models import Usuario


# Create your views here.

def home(request):
    return JsonResponse({'mensagem': 'Olá'})
 
def listar_usuarios(request):
    #Passo 1 -> ir no banco e trazer os usuarios

    usuarios = Usuario.objects.all()
    
    dados = []

    for usuario in usuarios:
        dados.append({
            'id': usuario.id, 
            'nome': usuario.nome,
            'email': usuario.email,
            'criado': usuario.criado.isoformat()
        })
    return JsonResponse({
            'usuarios': dados,
            'total': len(dados)
        })


