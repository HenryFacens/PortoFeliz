from django.shortcuts import render
from django.views.generic import View
from rest_framework import viewsets
from .models import Usuario, Proposta, Feedback, Geolocalizacao, Categoria, Tag, Noticia
from .serializers import UsuarioSerializer, PropostaSerializer, FeedbackSerializer, GeolocalizacaoSerializer, CategoriaSerializer, TagSerializer, NoticiaSerializer


class IndexView(View):
    def get(self, request):
        return render(request, 'index/base/base.html')

class MapView(View):
    def get(self, request):
        return render(request, 'map/base/base.html')

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PropostaViewSet(viewsets.ModelViewSet):
    queryset = Proposta.objects.all()
    serializer_class = PropostaSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class GeolocalizacaoViewSet(viewsets.ModelViewSet):
    queryset = Geolocalizacao.objects.all()
    serializer_class = GeolocalizacaoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer