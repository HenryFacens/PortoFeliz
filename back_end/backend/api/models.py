from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    data_join = models.DateField(auto_now_add=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_set',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='usuario',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_set',
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_query_name='usuario',
    )

class Proposta(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_criacao = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Geolocalizacao(models.Model):
    nome_setor = models.CharField(max_length=255)
    coordenadas = models.CharField(max_length=255)
    descricao = models.TextField()

class Feedback(models.Model):
    proposta = models.ForeignKey(Proposta, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    comentario = models.TextField()
    data_registro = models.DateField(auto_now_add=True)
    endereco = models.CharField(max_length=255)
    geo = models.ForeignKey(Geolocalizacao, on_delete=models.CASCADE)

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

class Tag(models.Model):
    nome = models.CharField(max_length=100)

class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    imagem = models.CharField(max_length=255)
    data_publicacao = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria, related_name='noticias')
    tags = models.ManyToManyField(Tag, related_name='noticias')
