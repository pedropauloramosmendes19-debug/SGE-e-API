from django.contrib import admin
from . import models


class OutflowAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'created_at',)
    search_fields = ('product__list',)


admin.site.register(models.Outflows, OutflowAdmin)


