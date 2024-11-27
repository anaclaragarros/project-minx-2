from rest_framework import serializers
from .models import Usuario
from .models import Seguir
from .models import Curtida
from .models import Postagem
from .models import Comentario
from django.contrib.auth.models import User


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields =  "__all__"

class SeguirSerializer(serializers.ModelSerializer):
    seguidor = serializers.StringRelatedField(read_only=True)
    seguindo = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Seguir
        fields = ['seguidor', 'seguindo', 'data_seguindo']


class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = '__all__'      


class CurtidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curtida
        fields = ['usuario', 'postagem', 'data_curtiu']        


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'
