from rest_framework import viewsets, filters
from .models import Factory, RetailNetwork, IndividualEntrepreneur
from .serializers import FactorySerializer, RetailNetworkSerializer, IndividualEntrepreneurSerializer
from .permissions import IsActiveEmployee  # Импортируем наш permission

class FactoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows factories to be viewed or edited.
    """
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['country', 'city'] # Добавлена фильтрация по городу
    permission_classes = [IsActiveEmployee]  # Применяем permission

class RetailNetworkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows retail networks to be viewed or edited.
    """
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['country', 'city'] # Добавлена фильтрация по городу
    permission_classes = [IsActiveEmployee]  # Применяем permission

class IndividualEntrepreneurViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows individual entrepreneurs to be viewed or edited.
    """
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['country', 'city'] # Добавлена фильтрация по городу
    permission_classes = [IsActiveEmployee]  # Применяем permission
