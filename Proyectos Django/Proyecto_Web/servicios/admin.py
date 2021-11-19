from django.contrib import admin

# Register your models here.
from servicios.models import Servicio
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')
    
admin.site.register(Servicio, ServicioAdmin)