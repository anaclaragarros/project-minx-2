from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib.auth.models import User
from .models import Usuario, Seguir, Postagem, Amizade, Curtida, Comentario
from .serializer import PostagemSerializer, CurtidaSerializer
from .serializer import UsuarioSerializer
from .serializer import SeguirSerializer
from .serializer import ComentarioSerializer
from rest_framework.permissions import IsAuthenticated



@api_view(['POST'])
def login_usuario(request):
   
    email = request.data.get('email')
    senha = request.data.get('senha')

    try:
        usuario = Usuario.objects.get(email=email, senha=senha)  
        serializer = UsuarioSerializer(usuario)  
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Usuario.DoesNotExist:
        return Response({'error': 'Usuário não encontrado ou credenciais inválidas'}, status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['POST'])
def createUsuario(request):
    
    data = request.data

    serializer = UsuarioSerializer(data=data)  
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response({'error':'Usuário inválido'}, status=status.HTTP_400_BAD_REQUEST)
    
  

@api_view(['POST'])
def seguirUsuario(request):
    
    seguidor_nome = request.data.get('seguidor_nome')
    seguindo_nome = request.data.get('seguindo_nome')

    try:
        seguidor = Usuario.objects.get(Usuario=seguidor_nome)
        seguindo = Usuario.objects.get(Usuario=seguindo_nome)

        if Seguir.objects.filter(seguidor=seguidor, seguindo=seguindo).exists():
            return Response({'mensagem': 'Já está seguindo este usuário'}, status=status.HTTP_400_BAD_REQUEST)

        seguir = Seguir.objects.create(seguidor=seguidor, seguindo=seguindo)
        serializer = SeguirSerializer(seguir)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except Usuario.DoesNotExist:
        return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)


    
@api_view(['POST'])
def criarPostagem(request):
    usuario = request.user 
    titulo = request.data.get('titulo')
    conteudo = request.data.get('conteudo')

    if not titulo or not conteudo:
        return Response({'error': 'Insira sua postagem'}, status=status.HTTP_400_BAD_REQUEST)

    postagem = Postagem.objects.create(usuario=usuario, titulo=titulo, conteudo=conteudo)
    serializer = PostagemSerializer(postagem)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def curtidaPostagem(request):
    usuario_nome = request.data.get('usuario_nome')  
    postagem_titulo = request.data.get('postagem_titulo') 

    try:
        usuario = Usuario.objects.get(nome=usuario_nome) 
        postagem = Postagem.objects.get(titulo=postagem_titulo) 
    except Usuario.DoesNotExist:
        return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    except Postagem.DoesNotExist:
        return Response({'error': 'Postagem não encontrada'}, status=status.HTTP_404_NOT_FOUND)

    if Curtida.objects.filter(usuario=usuario, postagem=postagem).exists():
        return Response({'mensagem': 'Você já curtiu esse post'}, status=status.HTTP_400_BAD_REQUEST)

    curtida = Curtida.objects.create(usuario=usuario, postagem=postagem)
    serializer = CurtidaSerializer(curtida)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def comentarioPostagem(request):
    usuario_nome = request.data.get('usuario_nome')  
    postagem_titulo = request.data.get('postagem_titulo')  
    conteudo = request.data.get('conteudo')  

    if not conteudo:
        return Response({'error': 'O conteúdo do comentário é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        usuario = Usuario.objects.get(nome=usuario_nome)  
        postagem = Postagem.objects.get(titulo=postagem_titulo) 
    except Usuario.DoesNotExist:
        return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    except Postagem.DoesNotExist:
        return Response({'error': 'Postagem não encontrada'}, status=status.HTTP_404_NOT_FOUND)

    comentario = comentario.objects.create(usuario=usuario, postagem=postagem, conteudo=conteudo)
    serializer = ComentarioSerializer(comentario)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def feed(request):
    usuario = request.user  
    amigos = Amizade.objects.filter(usuario1=usuario) | Amizade.objects.filter(usuario2=usuario)

    usuarios_amigos = [amizade.usuario2 if amizade.usuario1 == usuario else amizade.usuario1 for amizade in amigos]
    usuarios_amigos.append(usuario)  
 
    postagens = Postagem.objects.filter(usuario__in=usuarios_amigos).order_by('-data_criacao') 
    serializer = PostagemSerializer(postagens, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def feed(request):
    if not request.user.is_authenticated:
        return Response({'error': 'Você precisa estar logado para acessar o feed'}, status=status.HTTP_401_UNAUTHORIZED)
    
    usuario = request.user  
    amigos = Amizade.objects.filter(usuario1=usuario) | Amizade.objects.filter(usuario2=usuario)
    usuarios_amigos = [amizade.usuario2 if amizade.usuario1 == usuario else amizade.usuario1 for amizade in amigos]
    usuarios_amigos.append(usuario) 

    postagens = Postagem.objects.filter(usuario__in=usuarios_amigos).order_by('-data_criacao')
    serializer = PostagemSerializer(postagens, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
