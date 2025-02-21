from django.urls import path, include
from rest_framework import routers
from .views import FactoryViewSet, RetailNetworkViewSet, IndividualEntrepreneurViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'factories', FactoryViewSet)
router.register(r'retailnetworks', RetailNetworkViewSet)
router.register(r'entrepreneurs', IndividualEntrepreneurViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]