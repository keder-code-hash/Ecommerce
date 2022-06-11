from django.shortcuts import render

from .serializers.ShopModel import ShopModelSerializers
from .models.ShopModel import ShopModel

from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet

class ShopModelViewSet(ReadOnlyModelViewSet):
    queryset = ShopModel.objects.all()
    serializer_class = ShopModelSerializers
