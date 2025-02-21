from rest_framework import viewsets
from rest_framework import filters
from .models import Factory, RetailNetwork, IndividualEntrepreneur, Product
from .serializers import FactorySerializer, RetailNetworkSerializer, IndividualEntrepreneurSerializer, ProductSerializer
from rest_framework import permissions


class IsActiveEmployee(permissions.BasePermission):
    """
    Custom permission to only allow active employees to access the API.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_active


class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    permission_classes = [IsActiveEmployee]  # Только для активных сотрудников
    filter_backends = [filters.SearchFilter]
    search_fields = ['country']  # Фильтрация по стране


class RetailNetworkViewSet(viewsets.ModelViewSet):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [filters.SearchFilter]
    search_fields = ['country']


class IndividualEntrepreneurViewSet(viewsets.ModelViewSet):
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [filters.SearchFilter]
    search_fields = ['country']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'model']
