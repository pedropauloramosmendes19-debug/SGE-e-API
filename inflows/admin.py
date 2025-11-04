from django.contrib import admin
from . import models


class InflowAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'product', 'quantity', 'created_at',)
    search_fields = ('supplier__name', 'product__list',)


admin.site.register(models.Inflow, InflowAdmin)

