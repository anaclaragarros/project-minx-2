from django.urls import path
from . import views
from django.contrib.auth.models import User


urlpatterns = [
    
    path('login', views.login_usuario, name='login'),  
    path('create/usuario', views.createUsuario, name='create_usuario'),  
    path('usuario/seguir/', views.seguirUsuario, name='seguir_usuario'), 
    path('criar/postagem/', views.criarPostagem, name='criar_postagem'),
    path('curtida/postagem/', views.curtidaPostagem, name='curtida_postagem'),
    path('postagem/comentario/', views.comentarioPostagem, name='comentario_postagem'),
    path('feed/', views.feed, name='feed'),

    ]

    
