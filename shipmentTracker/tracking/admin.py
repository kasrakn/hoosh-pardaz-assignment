from django.contrib import admin
from tracking.models import ShipmentModel, WeatherModel

class ShipmentAdmin(admin.ModelAdmin):
    list_display = '__all__'

class WeatherAdmin(admin.ModelAdmin):
    list_display = '__all__'


admin.site.register(ShipmentModel, ShipmentAdmin)
admin.site.register(WeatherModel, WeatherAdmin)