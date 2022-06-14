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

from django.core import serializers
import json

class ShopModelViewSet(ReadOnlyModelViewSet):
    queryset = ShopModel.objects.all()
    serializer_class = ShopModelSerializers


# get carts details for an users.users can update the carts by adding produtcs or reving products


# get product for a particular shops for a particular or multiple filter
class TagProductModelViewSet(APIView): 

    def get(self,request,format = None):
        try :
            print(ProductModel.objects.filter(name__iexact = "Sharee1").values())
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode) 
            tags = body.get('tags')
            result = []
            instance = None
            for tag in tags :
                if instance is None:
                    instance = ProductModel.objects.filter(tags__name__iexact = tag).values()
                else:
                    instance = instance.filter(tags__name__iexact = tag)
            for inst in instance:
                prod_id = inst.get('id')
                Tag = Tagmodel.objects.filter(tags_product__id = prod_id).values()
                inst['tags'] = Tag
                result.append(inst)
            # serializer = ProductModelSerializers(data = result,many=True)
            # serializer.is_valid(raise_exception=True)
            return Response(result,status=status.HTTP_200_OK)
        except ProductModel.DoesNotExist:
            message = f"Inavalid request: Product Not Found: {tags}"
            raise APIException({"message": ValueError(message)}, message, 400)

            
#  makemeglobal.org@gmail.com