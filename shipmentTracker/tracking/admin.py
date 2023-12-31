from django.contrib import admin
from tracking.models import ShipmentModel, WeatherModel

class ShipmentAdmin(admin.ModelAdmin):
    pass
class WeatherAdmin(admin.ModelAdmin):
    pass


admin.site.register(ShipmentModel, ShipmentAdmin)
admin.site.register(WeatherModel, WeatherAdmin)