from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Dispositivo, Responsable, Servicio


class ResponsableResource(resources.ModelResource):
    class Meta:
        model = Responsable


class DispositivoResource(resources.ModelResource):
    class Meta:
        model = Dispositivo


class ServicioResource(resources.ModelResource):
    class Meta:
        model = Servicio


class ResponsableAdmin(ImportExportModelAdmin):
    resource_class = ResponsableResource
    list_display = ('nombre', 'apellido', 'cargo', 'id')
    search_fields = ('nombre',)


class DispositivoAdmin(ImportExportModelAdmin):
    resource_class = DispositivoResource
    list_display = (
        'activo_nuevo',
        'tipo_dispositivo',
        'marca',
        'modelo',
        'serial',
        'responsable'
    )
    search_fields = ('activo_nuevo',)


class ServicioAdmin(ImportExportModelAdmin):
    resource_class = ServicioResource
    list_display = (
        'tipo_servicio',
        'requerimiento',
        'solucion',
        'fecha',
        'dispositivos',
    )
    search_fields = ('dispositivos',)


# Registra tus modelos en el panel de administración
admin.site.register(Responsable, ResponsableAdmin)
admin.site.register(Dispositivo, DispositivoAdmin)
admin.site.register(Servicio, ServicioAdmin)
