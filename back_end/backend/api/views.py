from django.shortcuts import render
from django.views.generic import View
from rest_framework import viewsets
from .models import User, Sector, Interaction, Feedback, AdminUser
from .models import Sector, Interaction, Feedback, AdminUser
from .serializers import UserSerializer, SectorSerializer, InteractionSerializer, FeedbackSerializer, AdminUserSerializer, SuperUserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from api import serializers as api_serializers
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

class UserTokenSerializer(TokenObtainPairView):
    serializer_class = api_serializers.UserTokenSerializer

class IndexView(View):
    def get(self, request):
        return render(request, 'index/base/base.html')

class MapView(View):
    def get(self, request):
        return render(request, 'map/base/base.html')

# ViewSets define the view behavior.
class SuperUserViewSet(viewsets.ModelViewSet):
    UserAuth = get_user_model()
    queryset = UserAuth.objects.all()
    serializer_class = SuperUserSerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer
    permission_classes = [IsAuthenticated]

class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
    permission_classes = [IsAuthenticated]

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAuthenticated]
