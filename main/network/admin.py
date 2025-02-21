from django.contrib import admin
from .models import Factory, RetailNetwork, IndividualEntrepreneur, Product
from django.utils.html import format_html


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'get_supplier_link', 'debt')  # Отображаемые поля в списке
    list_filter = ('city',)  # Фильтр по городу
    actions = ['clear_debt']  # Admin action

    def get_supplier_link(self, obj):
        return None

    get_supplier_link.short_description = 'Поставщик'

    def clear_debt(self, request, queryset):
        """Admin action для очистки задолженности."""
        for obj in queryset:
            obj.debt = 0.00
            obj.save()

    clear_debt.short_description = "Очистить задолженность"


@admin.register(RetailNetwork)
class RetailNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'get_supplier_link', 'debt')
    list_filter = ('city',)
    actions = ['clear_debt']

    def get_supplier_link(self, obj):
        if obj.supplier:
            return format_html("<a href='/admin/network/factory/{}/change/'>{}</a>", obj.supplier.id, obj.supplier.name)
        return None

    get_supplier_link.short_description = 'Поставщик'

    def clear_debt(self, request, queryset):
        for obj in queryset:
            obj.debt = 0.00
            obj.save()

    clear_debt.short_description = "Очистить задолженность"


@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'get_supplier_link', 'debt')
    list_filter = ('city',)
    actions = ['clear_debt']

    def get_supplier_link(self, obj):
        if obj.supplier:
            return format_html("<a href='/admin/network/retailnetwork/{}/change/'>{}</a>", obj.supplier.id,
                               obj.supplier.name)
        return None

    get_supplier_link.short_description = 'Поставщик'

    def clear_debt(self, request, queryset):
        for obj in queryset:
            obj.debt = 0.00
            obj.save()

    clear_debt.short_description = "Очистить задолженность"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'factory', 'retail_network', 'individual_entrepreneur')
    list_filter = ('factory', 'retail_network', 'individual_entrepreneur')
