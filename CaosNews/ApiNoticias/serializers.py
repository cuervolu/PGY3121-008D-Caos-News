from rest_framework import serializers
from webcaosnews.models import Noticias


class NoticiaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Noticias
        fields = ["titulo","autor","fecha","categoria","portada","ubicacion"]