from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
   openapi.Info(
      title="Cidadania e Transparência API",
      default_version='v1',
      description="Documentação da API para o sistema de Cidadania e Transparência",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contato@seudominio.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'propostas', views.PropostaViewSet)
router.register(r'feedbacks', views.FeedbackViewSet)
router.register(r'geolocalizacoes', views.GeolocalizacaoViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'noticias', views.NoticiaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # API
    path('api/', include('api.urls')),
    path('', include('frontend.urls')),
    path('apiv2/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
