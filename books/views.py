from django.shortcuts import render
from rest_framework import generics
from .models import SEA_Book, SEA_Booksss
from .serializers import BookSerializer, BookSerializers


class BookAPIView(generics.ListCreateAPIView):
    queryset = SEA_Book.objects.all()
    serializer_class = BookSerializer


class BookDetailAPIVIEW(generics.RetrieveUpdateDestroyAPIView):
    queryset = SEA_Book.objects.all()
    serializer_class = BookSerializer


class BookAPIViews(generics.ListCreateAPIView):
    queryset = SEA_Booksss.objects.all()
    serializer_class = BookSerializers


class BookDetailAPIVIEWs(generics.RetrieveUpdateDestroyAPIView):
    queryset = SEA_Booksss.objects.all()
    serializer_class = BookSerializers
