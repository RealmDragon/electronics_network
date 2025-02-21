from django.db import models
from django.core.validators import MinValueValidator


class Supplier(models.Model):
    """Абстрактный класс поставщика."""
    name = models.CharField(max_length=255, verbose_name='Название')
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=255, verbose_name='Улица')
    house_number = models.CharField(max_length=20, verbose_name='Номер дома')
    debt = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
        validators=[MinValueValidator(0.00)],
        verbose_name='Задолженность перед поставщиком'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Factory(Supplier):
    """Завод."""
    pass

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'


class RetailNetwork(Supplier):
    """Розничная сеть."""
    supplier = models.ForeignKey('Factory', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Поставщик')

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'


class IndividualEntrepreneur(Supplier):
    """Индивидуальный предприниматель."""
    supplier = models.ForeignKey('RetailNetwork', on_delete=models.CASCADE, null=True, blank=True,
                                 verbose_name='Поставщик')

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальные предприниматели'


class Product(models.Model):
    """Продукт."""
    name = models.CharField(max_length=255, verbose_name='Название')
    model = models.CharField(max_length=255, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода на рынок')
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='products', verbose_name='Завод')
    retail_network = models.ForeignKey(RetailNetwork, on_delete=models.CASCADE, related_name='products', null=True,
                                       blank=True, verbose_name='Розничная сеть')
    individual_entrepreneur = models.ForeignKey(IndividualEntrepreneur, on_delete=models.CASCADE,
                                                related_name='products', null=True, blank=True,
                                                verbose_name='Индивидуальный предприниматель')

    def __str__(self):
        return f"{self.name} {self.model}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
