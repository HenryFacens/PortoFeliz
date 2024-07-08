from django.contrib import admin
from .models import Usuario, Proposta, Feedback, Geolocalizacao, Categoria, Tag, Noticia

admin.site.site_header = "Cidadania Transparente"
admin.site.site_title = "Cidadania Transparente"
admin.site.index_title = "Bem-vindo ao Portal de Cidadania Transparência"

admin.site.register(Usuario)
admin.site.register(Proposta)
admin.site.register(Feedback)
admin.site.register(Geolocalizacao)
admin.site.register(Categoria)
admin.site.register(Tag)
admin.site.register(Noticia)
