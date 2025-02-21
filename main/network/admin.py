from django.contrib import admin
from django.utils.html import format_html
from .models import Factory, RetailNetwork, IndividualEntrepreneur, Product


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'get_supplier_link', 'debt', 'created_at')
    list_filter = ('city', 'country')
    actions = ['clear_debt']

    def get_supplier_link(self, obj):
        return None  # У Factory нет поставщика
    get_supplier_link.short_description = 'Поставщик'

    def clear_debt(self, request, queryset):
        queryset.update(debt=0.00)  # Оптимизированный запрос
    clear_debt.short_description = "Очистить задолженность"


@admin.register(RetailNetwork)
class RetailNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'get_supplier_link', 'debt', 'created_at')
    list_filter = ('city', 'country')
    actions = ['clear_debt']

    def get_supplier_link(self, obj):
        if obj.supplier:
            url = f"/admin/network/factory/{obj.supplier.id}/change/"
            return format_html('<a href="{}">{}</a>', url, obj.supplier.name)
        return None
    get_supplier_link.short_description = 'Поставщик'

    def clear_debt(self, request, queryset):
        queryset.update(debt=0.00)  # Оптимизированный запрос
    clear_debt.short_description = "Очистить задолженность"


@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'get_supplier_link', 'debt', 'created_at')
    list_filter = ('city', 'country')
    actions = ['clear_debt']

    def get_supplier_link(self, obj):
        if obj.supplier:
            url = f"/admin/network/retailnetwork/{obj.supplier.id}/change/"
            return format_html('<a href="{}">{}</a>', url, obj.supplier.name)
        return None
    get_supplier_link.short_description = 'Поставщик'

    def clear_debt(self, request, queryset):
        queryset.update(debt=0.00)  # Оптимизированный запрос
    clear_debt.short_description = "Очистить задолженность"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')