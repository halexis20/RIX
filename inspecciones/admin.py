from django.contrib import admin
from inspecciones.models import Elemento,Equipo,Vulnerabilidad,Inspector,ModoDeFalla,Inspeccion,Foto,UserProfile,Componente,FuenteDeVulnerabilidad
# Register your models here.

@admin.register(FuenteDeVulnerabilidad)
class FuenteDeVulnerabilidadAdmin(admin.ModelAdmin):
    list_display=['id','nombre']

@admin.register(Componente)
class ComponenteAdmin(admin.ModelAdmin):
    list_display=['id','nombre','descripcion']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display=['id','user','role']

@admin.register(Elemento)
class ElementoAdmin(admin.ModelAdmin):
    list_display=['id','nombre','descripcion','padre']

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display=['id','tag','nombre','descripcion','elemento']

@admin.register(Vulnerabilidad)
class VulnerabilidadAdmin(admin.ModelAdmin):
    list_display=['id','nombre','valor']

@admin.register(Inspector)
class InspectorAdmin(admin.ModelAdmin):
    list_display=['id','nombre','mail']

@admin.register(ModoDeFalla)
class ModoDeFallaAdmin(admin.ModelAdmin):
    list_display=['id','nombre']

@admin.register(Inspeccion)
class InspeccionAdmin(admin.ModelAdmin):
    list_display=['id','fecha', 'inspector', 'vulnerabilidad', 'temperatura', 'vibracion', 'aviso']

@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display=['id','imagen']