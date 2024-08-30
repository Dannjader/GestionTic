from import_export import resources
from .models import Responsable, Dispositivo, Servicio


class ResponsableResource(resources.ModelResource):
    class Meta:
        model = Responsable
        fields = (
            'nombre',
            'apellido',
            'cargo'
        )

class DispositivoResource(resources.ModelResource):
    class Meta:
        model = Dispositivo
        fields = (
            'serial',
            'tipo_dispositivo',
            'marca',
            'modelo',
            'activo_viejo',
            'activo_nuevo',
            'ubicacion'
        )
        
class ServicioResource(resources.ModelResource):
    class Meta:
        model = Servicio
        fields = (
            'tipo_servicio',
            'requerimiento',
            'solucion',
            'fecha',
            'dispositivos'
        )