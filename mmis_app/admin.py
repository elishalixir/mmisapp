from django.contrib import admin
from .models import User, MercuryAddedProducts, EnergyConsumptionAndFuelProduction, Cement, EnvironmentAndHealth,\
    ASGMining


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['username', 'Fname', 'Sname', 'Organization_name', 'email']
    search_fields = ['username', 'Fname', 'Sname', 'Organization_name', 'email']


class MercuryAddedProductsAdmin(admin.ModelAdmin):
    list_display = ['author', 'mercury_compound', 'item', 'imported', 'consumption_or_production',
                    'year',  'created_at']
    list_per_page = 10
    search_fields = ['mercury_compound', 'item', 'imported', 'consumption_or_production',
                     'year', 'created_at']


class EnergyConsumptionAndFuelProductionAdmin(admin.ModelAdmin):
    list_display = ['author', 'energy_fuel', 'imported', 'consumption_or_production',
                    'year', 'created_at']
    list_per_page = 10
    search_fields = ['energy_fuel', 'imported', 'consumption_or_production',
                     'year', 'created_at']


class CementAdmin(admin.ModelAdmin):
    list_display = ['author', 'operation_cover', 'yes', 'consumption_or_production',
                    'year', 'created_at']
    list_per_page = 10
    search_fields = ['energy_fuel', 'yes', 'consumption_or_production',
                     'year', 'created_at']


class EnvironmentAndHealthAdmin(admin.ModelAdmin):
    list_display = ['submitted',  'created_at']
    list_per_page = 10


class ASGMiningAdmin(admin.ModelAdmin):
    list_display = ['submitted',  'created_at']
    list_per_page = 10


admin.site.register(User, UserAdmin)
admin.site.register(MercuryAddedProducts, MercuryAddedProductsAdmin)
admin.site.register(EnergyConsumptionAndFuelProduction, EnergyConsumptionAndFuelProductionAdmin)
admin.site.register(Cement, CementAdmin)
admin.site.register(EnvironmentAndHealth, EnvironmentAndHealthAdmin)
admin.site.register(ASGMining, ASGMiningAdmin)
