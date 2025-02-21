from rest_framework import serializers
from .models import Factory, RetailNetwork, IndividualEntrepreneur, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class FactorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)  # Для отображения продуктов завода

    class Meta:
        model = Factory
        fields = '__all__'
        read_only_fields = ('debt',)  # Запрещаем изменение поля debt


class RetailNetworkSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)  # Для отображения продуктов розничной сети

    class Meta:
        model = RetailNetwork
        fields = '__all__'
        read_only_fields = ('debt',)  # Запрещаем изменение поля debt


class IndividualEntrepreneurSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)  # Для отображения продуктов ИП

    class Meta:
        model = IndividualEntrepreneur
        fields = '__all__'
        read_only_fields = ('debt',)  # Запрещаем изменение поля debt
