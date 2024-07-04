from django.urls import path, include
from frontend.views import IndexView, MapView

urlpatterns = [
    #Pages
    path('',IndexView.as_view(), name='home'),
    path('map/',MapView.as_view(), name='map'),

    ]
