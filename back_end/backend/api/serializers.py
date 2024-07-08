from rest_framework import serializers
from .models import Usuario, Proposta, Feedback, Geolocalizacao, Categoria, Tag, Noticia

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class PropostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposta
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class GeolocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocalizacao
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'
