from django.shortcuts import render
from django.views.generic import View
from rest_framework import viewsets
from .models import User, Sector, Interaction, Feedback, AdminUser
from .serializers import UserSerializer, SectorSerializer, InteractionSerializer, FeedbackSerializer, AdminUserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from api import serializers as api_serializers

class UserTokenSerializer(TokenObtainPairView):
    serializer_class = api_serializers.UserTokenSerializer

class IndexView(View):
    def get(self, request):
        return render(request, 'index/base/base.html')

class MapView(View):
    def get(self, request):
        return render(request, 'map/base/base.html')
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer
