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
    path('elemento/<int:elemento_id>/create',elemento_create,name='elemento_create'),
    path('elemento/create',elemento_create_base,name='elemento_create'),
    path('elemento/<int:elemento_id>/update',elemento_update,name='elemento_update'),
    path('elemento/<int:elemento_id>/delete',elemento_delete,name='elemento_delete'),
    path('elemento',elemento_list,name='elemento_list'),
    path('equipo/<int:elemento_id>/create',equipo_create,name='equipo_create'),
    path('equipo/<int:equipo_id>/update',equipo_update,name='equipo_update'),
    path('equipo/<int:equipo_id>/delete',equipo_delete,name='equipo_delete'),
    path('vulnerabilidad',vulnerabilidad_list,name='vulnerabilidad_list'),
    path('vulnerabilidad/create',vulnerabilidad_create,name='vulnerabilidad_create'),
    path('vulnerabilidad/<int:vulnerabilidad_id>/update',vulnerabilidad_update,name='vulnerabilidad_update'),
    path('vulnerabilidad/<int:vulnerabilidad_id>/delete',vulnerabilidad_delete,name='vulnerabilidad_delete'),
    path('inspector',inspector_list,name='inspector_list'),
    path('inspector/create',inspector_create,name='inspector_create'),
    path('inspector/<int:inspector_id>/update',inspector_update,name='inspector_update'),
    path('inspector/<int:inspector_id>/delete',inspector_delete,name='inspector_delete'),
    path('mododefalla',mododefalla_list,name='mododefalla_list'),
    path('mododefalla/create',mododefalla_create,name='mododefalla_create'),
    path('mododefalla/<int:mododefalla_id>/update',mododefalla_update,name='mododefalla_update'),
    path('mododefalla/<int:mododefalla_id>/delete',mododefalla_delete,name='mododefalla_delete'),
    path('inspeccion',inspeccion_list,name='inspeccion_list'),
    path('inspeccion/create',inspeccion_create,name='inspeccion_create'),
    path('inspeccion/<int:inspeccion_id>/update',inspeccion_update,name='inspeccion_update'),
    path('inspeccion/<int:inspeccion_id>/delete',inspeccion_delete,name='inspeccion_delete'),
    path('inspeccion/<int:inspeccion_id>/pdf',inspeccion_pdf,name='inspeccion_pdf'),
    path('inspeccion/ultimas_inspecciones',ultimas_inspecciones,name='ultimas_inspecciones'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',custom_logout,name='logout'),
    path('sinpermisos',sin_permisos,name='sinpermisos'),
    path('componente/<int:equipo_id>/create',componente_create,name='componente_create'),
    path('componente/<int:componente_id>/update',componente_update,name='componente_update'),
    path('componente/<int:componente_id>/delete',componente_delete,name='componente_delete'),
    path('fuentedevulnerabilidad',fuentedevulnerabilidad_list,name='fuentedevulnerabilidad_list'),
    path('fuentedevulnerabilidad/create',fuentedevulnerabilidad_create,name='fuentedevulnerabilidad_create'),
    path('fuentedevulnerabilidad/<int:fuentedevulnerabilidad_id>/update',fuentedevulnerabilidad_update,name='fuentedevulnerabilidad_update'),
    path('fuentedevulnerabilidad/<int:fuentedevulnerabilidad_id>/delete',fuentedevulnerabilidad_delete,name='fuentedevulnerabilidad_delete'),
    path('componente',componente_list,name='componente_list'),
    path('mapasemanal',reporte_probabilidades_semana,name='reporte_probabilidades_semana'),
    path('diagramaplanta',valor_maximo_vulnerabilidad,name='diagramaplanta'),
    path('probabilidadxequipoxactual',valores_maximos_vulnerabilidad_equipo,name='vulnerabilidadmaxima'),
    path('usuario/create',user_create,name='usuario_create'),
    path('usuario',user_list,name='usuario_list'),
    path('usuario/<int:user_id>/update',user_update,name='usuario_update'),
    path('usuario/<int:user_id>/desactivate',user_desactivate,name='usuario_desactivate')
]
