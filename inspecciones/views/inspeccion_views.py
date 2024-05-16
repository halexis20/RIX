from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ..models import Inspeccion,Foto,Componente
from ..forms import InspeccionForm,FotoForm
from .utils import admin_required, render_template
from django.db.models import Max


@login_required
def inspeccion_list(request):
    inspecciones = Inspeccion.objects.all().order_by('fecha')
    return render(request, 'inspeccion/list.html', {'inspecciones': inspecciones})


@login_required
def inspeccion_create(request):
    if request.method == 'POST':
        inspeccionform = InspeccionForm(request.POST)
        fotoform=FotoForm(request.POST,request.FILES)
        if inspeccionform.is_valid() and fotoform.is_valid():
            inspeccion=inspeccionform.save()
            for imagen in request.FILES.getlist('imagenes'):
                foto = Foto(inspeccion=inspeccion, imagen=imagen)
                foto.save()
            return redirect('inspeccion_list')
    else:
        inspeccionform = InspeccionForm()
        fotoform=FotoForm()
        inspeccionform.fields['componente'].queryset = Componente.objects.all().order_by('nombre')
    return render(request, 'inspeccion/create.html', {'inspeccionform': inspeccionform,'fotoform':fotoform})

@login_required
def inspeccion_update(request, inspeccion_id):
    inspeccion = get_object_or_404(Inspeccion, pk=inspeccion_id)
    if request.method == 'POST':
        form = InspeccionForm(request.POST, instance=inspeccion)
        fotoform = FotoForm(request.POST, request.FILES)
        if form.is_valid() and fotoform.is_valid():
            # Guardar el formulario de inspección
            form.save()

            # Procesar las nuevas fotos
            for imagen in request.FILES.getlist('imagenes'):
                foto = Foto(inspeccion=inspeccion, imagen=imagen)
                foto.save()

            # Eliminar las fotos desvinculadas si se han marcado para eliminar
            fotos_desvinculadas_ids = request.POST.getlist('eliminar_fotos')
            Foto.objects.filter(id__in=fotos_desvinculadas_ids).delete()

            return redirect('inspeccion_list')
    else:
        inspeccion_fecha_iso8601 = inspeccion.fecha.strftime('%Y-%m-%d %H:%M:%S')
        if inspeccion.fechaplaneada :
            inspeccion_fechaplaneada_iso8601=inspeccion.fechaplaneada.strftime('%Y-%m-%d')
        else:
            inspeccion_fechaplaneada_iso8601=""
        form = InspeccionForm(instance=inspeccion,initial={'fecha': inspeccion_fecha_iso8601,'fechaplaneada':inspeccion_fechaplaneada_iso8601})
        fotoform = FotoForm()
        # Obtener todas las fotos relacionadas con la inspección existente
        fotos = inspeccion.fotos.all()
        # Puedes agregar esta línea si deseas ordenar los equipos por tag en el formulario
        form.fields['componente'].queryset = Componente.objects.all().order_by('nombre')


    return render(request, 'inspeccion/update.html', {'form': form, 'inspeccion': inspeccion, 'fotoform': fotoform, 'fotos': fotos,'inspeccion_fecha_iso8601':inspeccion_fecha_iso8601})

@admin_required
def inspeccion_delete(request,inspeccion_id):
        inspeccion=get_object_or_404(Inspeccion,pk=inspeccion_id)
        if request.method=='POST':
            inspeccion.delete()
            return redirect('inspeccion_list')
        else:
            return render(request,'inspeccion/confirm_delete.html',{'inspeccion':inspeccion})


@login_required
def inspeccion_pdf(request, inspeccion_id):
    inspeccion = get_object_or_404(Inspeccion, pk=inspeccion_id)
    
    return render(request,'inspeccion/pdf_template.html',{'inspeccion':inspeccion})

@login_required
def ultimas_inspecciones(request):
    # Obtener la fecha más reciente de cada equipo
    fechas_maximas = Inspeccion.objects.values('componente').annotate(max_fecha=Max('fecha'))

    # Filtrar las inspecciones que coincidan con las fechas máximas por equipo
    ultimas_inspecciones = Inspeccion.objects.filter(componente__in=fechas_maximas.values('componente'), fecha__in=fechas_maximas.values('max_fecha')).order_by('-fecha')

    return render(request, 'inspeccion/ultimas_inspecciones.html', {'ultimas_inspecciones': ultimas_inspecciones})