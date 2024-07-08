from django.contrib import admin
from django.urls import path, include
from api.views import UserTokenSerializer

urlpatterns = [
    path('user/token/', UserTokenSerializer.as_view(), name='token_obtain_pair'),
    ]


