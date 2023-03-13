from django.contrib import admin

from categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
        'created_at',
        'updated_at'
    ]