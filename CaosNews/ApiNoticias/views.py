from .serializers import NoticiaSerializers
from rest_framework import generics
from webcaosnews.models import Noticias
from rest_framework.views import APIView
import datetime

# Create your views here.
class NoticiasViewSet(generics.ListAPIView):
    queryset = Noticias.objects.filter(aprobada=True)
    serializer_class = NoticiaSerializers
    
class NoticiasBuscarViewSet(generics.ListAPIView):
    serializer_class = NoticiaSerializers
    def get_queryset(self):
        nombre_noticia = self.kwargs["categoria"]
        return Noticias.objects.filter(categoria = nombre_noticia)
   