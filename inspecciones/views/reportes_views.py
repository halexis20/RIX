from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from ..models import Inspeccion,Componente
from .utils import admin_required,render_template
from django.utils import timezone
from django.db.models import Max
from datetime import timedelta
from django.http import JsonResponse

@login_required
def reporte_probabilidades_semana(request):
    # Obtener el año actual
    años_disponibles = Inspeccion.objects.values_list('fecha__year', flat=True).distinct()
    semanas = range(1, 53)
    año_actual = request.GET.get('año', None)
    año_actual = int(año_actual) if año_actual else None

    # Si no se proporciona un claño, usar el año actual
    if año_actual is None:
        año_actual = timezone.now().year

    # Obtener todos los componentes
    componentes = Componente.objects.all()

    # Crear un diccionario para almacenar los datos del informe
    reporte = {}

    # Obtener el número total de semanas en el año
    num_semanas = 52

    # Iterar sobre cada componente
    for componente in componentes:
        # Crear una entrada en el diccionario de informes para este componente
        reporte[componente] = {}

        # Iterar sobre cada semana del año
        for semana in range(1, num_semanas + 1):
            # Obtener la fecha de inicio y fin de la semana
            fecha_inicio_semana = timezone.make_aware(timezone.datetime(año_actual, 1, 1)) + timedelta(weeks=semana - 1)
            fecha_fin_semana = fecha_inicio_semana + timedelta(days=6)

            # Filtrar inspecciones para este componente y esta semana
            inspecciones = Inspeccion.objects.filter(
                componente=componente,
                fecha__range=(fecha_inicio_semana, fecha_fin_semana)
            ).order_by('-fecha')

            # Obtener la última inspección de esta semana
            ultima_inspeccion = inspecciones.first()

            # Si no hay inspecciones en esta semana, usar la última inspección anterior
            if not ultima_inspeccion:
                inspeccion_anterior = Inspeccion.objects.filter(
                    componente=componente,
                    fecha__lt=fecha_inicio_semana
                ).order_by('-fecha').first()
                if inspeccion_anterior:
                    vulnerabilidad = inspeccion_anterior.vulnerabilidad.valor
                    color = inspeccion_anterior.vulnerabilidad.color
                else:
                    vulnerabilidad = None
                    color = '#000000'
            else:
                vulnerabilidad = ultima_inspeccion.vulnerabilidad.valor
                color = ultima_inspeccion.vulnerabilidad.color


            # Almacenar la vulnerabilidad en el diccionario de informes
            reporte[componente][semana] = {'vulnerabilidad': vulnerabilidad, 'color': color}

    # Renderizar el template con los datos del informe
    return render(request, 'reporte_probabilidades_semanal.html', {'reporte': reporte, 'año_actual': año_actual,'años_disponibles':años_disponibles,'semanas':semanas})




@login_required
def valor_maximo_vulnerabilidad(request):

    return render(request, 'diagramaplanta.html')


def valores_maximos_vulnerabilidad_equipo(request):

    # Obtener la fecha más reciente de cada componente
    fechas_maximas = Inspeccion.objects.values('componente').annotate(max_fecha=Max('fecha'))

    # Filtrar las inspecciones que coincidan con las fechas máximas por componente
    ultimas_inspecciones = Inspeccion.objects.filter(componente__in=fechas_maximas.values('componente'), fecha__in=fechas_maximas.values('max_fecha'))

    # Crear un diccionario para almacenar los valores máximos y colores de vulnerabilidad por equipo
    valores_maximos_vulnerabilidad = {}

    # Iterar sobre las últimas inspecciones de cada componente
    for inspeccion in ultimas_inspecciones:
        equipo_id = inspeccion.componente.equipo.id
        valor_vulnerabilidad = inspeccion.vulnerabilidad.valor
        color_vulnerabilidad = inspeccion.vulnerabilidad.color
        equipo_tag= inspeccion.componente.equipo.tag

        # Actualizar el valor máximo de vulnerabilidad para el equipo
        if equipo_tag not in valores_maximos_vulnerabilidad:
            valores_maximos_vulnerabilidad[equipo_tag] = {'valor': valor_vulnerabilidad, 'color': color_vulnerabilidad}
        else:
            if valor_vulnerabilidad > valores_maximos_vulnerabilidad[equipo_tag]['valor']:
                valores_maximos_vulnerabilidad[equipo_tag] = {'valor': valor_vulnerabilidad, 'color': color_vulnerabilidad}


    return JsonResponse(valores_maximos_vulnerabilidad)
