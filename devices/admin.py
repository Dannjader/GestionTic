from django.contrib import admin
from devices.models import Dispositivo, Responsable, Servicio
# Register your models here.
admin.site.register(Dispositivo)
admin.site.register(Responsable)
admin.site.register(Servicio)
