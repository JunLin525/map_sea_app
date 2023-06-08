from django.shortcuts import render
from rest_framework import generics
from .models import SEA_MAP
from .serializers import MapSerializer

# Create your views here.


class MAPAPIView(generics.ListCreateAPIView):
    queryset = SEA_MAP.objects.all()
    serializer_class = MapSerializer


class MapDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SEA_MAP.objects.all()
    serializer_class = MapSerializer
