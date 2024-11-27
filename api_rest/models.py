from django.db import models
from api_root import settings
from django.contrib.auth.models import User
from django.conf import settings


class Usuario(models.Model):
    nome = models.CharField(max_length=100, default="Usuário Desconhecido")
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100, default="123456")

    def __str__(self):
        return f'Usuario: {self.nome} | {self.email} | {self.senha}'



class Seguir(models.Model):
    seguidor = models.ForeignKey('Usuario', related_name='seguindo', on_delete=models.CASCADE)
    seguindo = models.ForeignKey('Usuario', related_name='seguidores', on_delete=models.CASCADE)
    data_seguindo = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('seguidor', 'seguindo')

    def __str__(self):
        return f"{self.seguidor.nome} segue {self.seguindo.nome}"
    

class Postagem(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Curtida(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name="curtidas")
    postagem = models.ForeignKey('Postagem', on_delete=models.CASCADE, related_name="curtidas")
    data_curtiu = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['usuario', 'postagem'], name='unique_usuario_postagem')
        ]

    def __str__(self):
        return f'{self.usuario.nome} curtiu {self.postagem.titulo}'


class Comentario(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name="comentarios")
    postagem = models.ForeignKey('Postagem', on_delete=models.CASCADE, related_name="comentarios")
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.nome} comentou em {self.postagem.titulo}"
    

class Amizade(models.Model):
    usuario1 = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='amigo1')
    usuario2 = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='amigo2')
    data_amizade = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario1.username} e {self.usuario2.username} são amigos'
