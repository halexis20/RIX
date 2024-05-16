from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls import handler404
from django.shortcuts import render

from .views.user_views import (custom_logout,user_list,user_create,user_update,user_desactivate)
from .views.elemento_views import (elemento_list,elemento_create,elemento_create_base,elemento_update,elemento_delete)
from .views.equipo_views import (equipo_create,equipo_update,equipo_delete)
from .views.componente_views import (componente_list,componente_create,componente_update,componente_delete)
from .views.inspector_views import (inspector_list, inspector_create, inspector_update, inspector_delete)
from .views.vulnerabilidad_views import (vulnerabilidad_list,vulnerabilidad_create,vulnerabilidad_update,vulnerabilidad_delete)
from .views.fuentedevulnerabilidad_views import (fuentedevulnerabilidad_list,fuentedevulnerabilidad_create,fuentedevulnerabilidad_update,fuentedevulnerabilidad_delete)
from .views.mododefalla_views import (mododefalla_list,mododefalla_create,mododefalla_update,mododefalla_delete)
from .views.inspeccion_views import (inspeccion_list,inspeccion_create,inspeccion_update,inspeccion_delete,inspeccion_pdf,ultimas_inspecciones)
from .views.reportes_views import (reporte_probabilidades_semana,valor_maximo_vulnerabilidad,valores_maximos_vulnerabilidad_equipo)
from .views.utils import (sin_permisos)

urlpatterns=[
    path('elementos/create/<int:elemento_id>',elemento_create,name='elemento_create'),
    path('elementos/create',elemento_create_base,name='elemento_create'),
    path('elementos/update/<int:elemento_id>',elemento_update,name='elemento_update'),
    path('elementos/delete/<int:elemento_id>',elemento_delete,name='elemento_delete'),
    path('elementos',elemento_list,name='elemento_list'),
    path('equipos/create/<int:elemento_id>',equipo_create,name='equipo_create'),
    path('equipos/update/<int:equipo_id>',equipo_update,name='equipo_update'),
    path('equipos/delete/<int:equipo_id>',equipo_delete,name='equipo_delete'),
    path('vulnerabilidades',vulnerabilidad_list,name='vulnerabilidad_list'),
    path('vulnerabilidades/create',vulnerabilidad_create,name='vulnerabilidad_create'),
    path('vulnerabilidades/update/<int:vulnerabilidad_id>',vulnerabilidad_update,name='vulnerabilidad_update'),
    path('vulnerabilidades/delete/<int:vulnerabilidad_id>',vulnerabilidad_delete,name='vulnerabilidad_delete'),
    path('inspectores',inspector_list,name='inspector_list'),
    path('inspectores/create',inspector_create,name='inspector_create'),
    path('inspectores/update/<int:inspector_id>',inspector_update,name='inspector_update'),
    path('inspectores/delete/<int:inspector_id>',inspector_delete,name='inspector_delete'),
    path('modosdefalla',mododefalla_list,name='mododefalla_list'),
    path('modosdefalla/create',mododefalla_create,name='mododefalla_create'),
    path('modosdefalla/update/<int:mododefalla_id>',mododefalla_update,name='mododefalla_update'),
    path('modosdefalla/delete/<int:mododefalla_id>',mododefalla_delete,name='mododefalla_delete'),
    path('inspeccion',inspeccion_list,name='inspeccion_list'),
    path('inspecciones/create',inspeccion_create,name='inspeccion_create'),
    path('inspecciones/update/<int:inspeccion_id>',inspeccion_update,name='inspeccion_update'),
    path('inspecciones/delete/<int:inspeccion_id>',inspeccion_delete,name='inspeccion_delete'),
    path('inspecciones/pdf/<int:inspeccion_id>',inspeccion_pdf,name='inspeccion_pdf'),
    path('inspecciones/ultimas_inspecciones',ultimas_inspecciones,name='ultimas_inspecciones'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',custom_logout,name='logout'),
    path('sinpermisos',sin_permisos,name='sinpermisos'),
    path('componentes/create/<int:equipo_id>',componente_create,name='componente_create'),
    path('componentes/update/<int:componente_id>',componente_update,name='componente_update'),
    path('componentes/delete/<int:componente_id>',componente_delete,name='componente_delete'),
    path('fuentesdevulnerabilidad',fuentedevulnerabilidad_list,name='fuentedevulnerabilidad_list'),
    path('fuentesdevulnerabilidad/create',fuentedevulnerabilidad_create,name='fuentedevulnerabilidad_create'),
    path('fuentesdevulnerabilidad/update/<int:fuentedevulnerabilidad_id>',fuentedevulnerabilidad_update,name='fuentedevulnerabilidad_update'),
    path('fuentesdevulnerabilidad/delete/<int:fuentedevulnerabilidad_id>',fuentedevulnerabilidad_delete,name='fuentedevulnerabilidad_delete'),
    path('componentes',componente_list,name='componente_list'),
    path('mapasemanal',reporte_probabilidades_semana,name='reporte_probabilidades_semana'),
    path('diagramaplanta',valor_maximo_vulnerabilidad,name='diagramaplanta'),
    path('probabilidadxequipoxactual',valores_maximos_vulnerabilidad_equipo,name='vulnerabilidadmaxima'),
    path('usuarios/create',user_create,name='usuario_create'),
    path('usuarios',user_list,name='usuario_list'),
    path('usuarios/update/<int:user_id>',user_update,name='usuario_update'),
    path('usuarios/desactivate/<int:user_id>',user_desactivate,name='usuario_desactivate')
]
