from django.urls import path, include
from drf_yasg.views import get_schema_view
from api import views
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
   openapi.Info(
      title="Cidadania e Transparência API",
      default_version='v1',
      description="Documentação da API para o sistema de Cidadania e Transparência",
      contact=openapi.Contact(email="h3nry.almeida@gmail.com"),
      license=openapi.License(name="Presturion License"),
   ),
   public=False,
   permission_classes=(AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'userAuth', views.SuperUserViewSet,basename='userauth')
router.register(r'sectors', views.SectorViewSet)
router.register(r'interactions', views.InteractionViewSet)
router.register(r'feedbacks', views.FeedbackViewSet)
router.register(r'adminusers', views.AdminUserViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Generate Token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
