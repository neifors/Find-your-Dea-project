from django.apps import AppConfig
import os, json


class FinderConfig(AppConfig):
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'finder'
    
    def ready(self):
        dinamic_path = os.path.realpath(__file__)[0:-8]
        
        def get_data():
            with open (f"{dinamic_path}\deas.json", encoding="utf8") as file:
                return json.load(file)
            
        # data = get_data()
        def inster_into(dataset):
            from .models import Dea
            for dea in dataset:
                Dea.objects.create(codigo_dea=dea["codigo_dea"],direccion_ubicacion=dea["direccion_ubicacion"],direccion_via_codigo=dea["direccion_via_codigo"],direccion_via_nombre=dea["direccion_via_nombre"],direccion_portal_numero=dea["direccion_portal_numero"],direccion_codigo_postal=dea["direccion_codigo_postal"],horario_acceso=dea["horario_acceso"],x_utm=int(dea["direccion_coordenada_x"]),y_utm=int(dea["direccion_coordenada_y"]))

        # inster_into(data)
        
