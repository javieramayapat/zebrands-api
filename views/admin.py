from django.contrib import admin
from views.models import View


@admin.register(View)
class ViewAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'viewed_at',
    ]