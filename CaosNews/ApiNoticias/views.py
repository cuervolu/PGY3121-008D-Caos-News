from django.shortcuts import render
from .serializers import NoticiaSerializers
from rest_framework import generics
from webcaosnews.models import Noticias

# Create your views here.
class NoticiasViewSet(generics.ListAPIView):
    queryset = Noticias.objects.all()
    serializer_class = NoticiaSerializers
    
class NoticiasBuscarViewSet(generics.ListAPIView):
    serializer_class = NoticiaSerializers
    def get_queryset(self):
        nombre_noticia = self.kwargs["categoria"]
        return Noticias.objects.filter(categoria = nombre_noticia)