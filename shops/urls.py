from django.urls import path
from django.urls.conf import include

from rest_framework.routers import DefaultRouter

from .views import ShopModelViewSet

router = DefaultRouter()
router.register(r'API/shops',ShopModelViewSet ,basename="register")

urlpatterns=[
    path('',include(router.urls))
]