from django.urls import path
from django.urls.conf import include

from rest_framework.routers import DefaultRouter,SimpleRouter

from .views import ShopModelViewSet,TagProductModelViewSet

router = DefaultRouter()
router.register(r'API/fetchshops',ShopModelViewSet ,basename="shops") 

urlpatterns=[
    path('',include(router.urls)),
    path('API/poductbytags/<tags>',TagProductModelViewSet.as_view(),name = "tagfilter")
]