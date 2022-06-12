from django.shortcuts import get_object_or_404, render

from .serializers.ShopModel import ShopModelSerializers
from .models.ShopModel import ShopModel
from .models.TagModel import Tagmodel
from .models.ProductModel import ProductModel
from .serializers.TagModel import TagModelSerializers
from .serializers.ProductModel import ProductModelSerializers

from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet

from django.shortcuts import get_object_or_404
from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.views import Response,APIView

import json

class ShopModelViewSet(ReadOnlyModelViewSet):
    queryset = ShopModel.objects.all()
    serializer_class = ShopModelSerializers


# get carts details for an users.users can update the carts by adding produtcs or reving products


# get product for a particular shops for a particular or multiple filter
class TagProductModelViewSet(APIView): 

    def get(self,request,format = None):
        try :

            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode) 
            tags = body.get('tags')

            instance = None
            for tag in tags :
                if instance is None:
                    instance = ProductModel.objects.filter(related_tags__name__iexact = tag)
                else:
                    instance = instance.filter(related_tags__name__iexact = tag)
            instance = instance.values()

            instance = get_object_or_404(instance)
            serializer = ProductModelSerializers(data = instance,many=True)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except ProductModel.DoesNotExist:
            message = f"Inavalid request: Product Not Found: {tags}"
            raise APIException({"message": ValueError(message)}, message, 400)
 
