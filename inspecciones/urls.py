from django.urls import path
from .views import elemento_list,elemento_create_base,elemento_create,elemento_update,elemento_delete,atributo_create,atributo_update,atributo_delete,vulnerabilidad_list,vulnerabilidad_create,vulnerabilidad_update,vulnerabilidad_delete,inspector_list,inspector_create,inspector_update,inspector_delete,mododefalla_list,mododefalla_create,mododefalla_update,mododefalla_delete,inspeccion_list,inspeccion_create,inspeccion_update,inspeccion_delete,inspeccion_pdf,ultimas_inspecciones,custom_logout,sin_permisos,dashboard
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls import handler404
from django.shortcuts import render

urlpatterns=[
    path('elemento/<int:elemento_id>/create',elemento_create,name='elemento_create'),
    path('elemento/create',elemento_create_base,name='elemento_create'),
    path('elemento/<int:elemento_id>/update',elemento_update,name='elemento_update'),
    path('elemento/<int:elemento_id>/delete',elemento_delete,name='elemento_delete'),
    path('elemento',elemento_list,name='elemento_list'),
    path('atributo/<int:elemento_id>/create',atributo_create,name='atributo_create'),
    path('atributo/<int:atributo_id>/update',atributo_update,name='atributo_update'),
    path('atributo/<int:atributo_id>/delete',atributo_delete,name='atributo_delete'),
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
    path('dashboard',dashboard,name='dashboard')
]
