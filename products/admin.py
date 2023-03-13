from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "sku",
        "brand",
        "name",
        "price",
        "description",
        "category",
        "created_at",
        "updated_at",
    ]
