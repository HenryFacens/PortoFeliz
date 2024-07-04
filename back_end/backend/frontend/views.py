from django.shortcuts import render
from django.views.generic import View
from frontend.tools.map import Map

class IndexView(View):
    def get(self, request):
        return render(request, 'index/base/base.html')

class MapView(View):
    def get(self, request):
        return render(request, 'map/base/base.html')