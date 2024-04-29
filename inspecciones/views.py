from django.shortcuts import render,get_object_or_404,redirect
from .models import Elemento,Atributo,Vulnerabilidad,Inspector,ModoDeFalla,Inspeccion,Foto
from .forms import ElementoForm,AtributoForm,VulnerabilidadForm,InspectorForm,ModoDeFallaForm,InspeccionForm,FotoForm
from django.http import HttpRequest
from django.contrib import messages
from django import forms

from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from django.db.models import Max

from django.db.models import Count, Avg

# Create your views here.

def sin_permisos(request):
    
    return render(request,'sinpermisos.html',{})  

def custom_logout(request):
    from django.contrib.auth import logout
    logout(request)
    
    return redirect('login')  

@login_required
def elemento_list(request):
    if request.user.userprofile.role == 'admin':
        elementos=Elemento.objects.all().order_by('nombre')
        return render(request,'elemento/list.html',{'elementos':elementos})
    else:
        return redirect('sinpermisos')

@login_required
def elemento_create(request,elemento_id):
    elemento= get_object_or_404(Elemento,pk=elemento_id)
    if request.method=='POST':
        form=ElementoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('elemento_list')
    else:
        form = ElementoForm(initial={'padre': elemento})
        form.fields['padre'].widget = forms.HiddenInput()
    return render(request,'elemento/create2.html',{'form':form,'elemento':elemento})

@login_required
def elemento_delete(request, elemento_id):
    # Obtener el elemento a eliminar
    elemento = get_object_or_404(Elemento, pk=elemento_id)

    if request.method == 'POST':
        elemento.delete()
        return redirect('elemento_list')
    else:
        return render(request, 'elemento/confirm_delete.html', {'elemento': elemento})

@login_required
def elemento_create_base(request):
    elementos=Elemento.objects.all()
    if request.method=='POST':
        form=ElementoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('elemento_list')
    else:
        form=ElementoForm()
    
    return render(request,'elemento/create.html',{'form':form,'elementos':elementos})

@login_required
def elemento_update(request,elemento_id):
    elemento=get_object_or_404(Elemento,pk=elemento_id)
    if request.method=='POST':
        form=ElementoForm(request.POST,instance=elemento)
        if form.is_valid():
            form.save()
            return redirect('elemento_list')
        
    else:
        form=ElementoForm(instance=elemento)

    return render(request,'elemento/update.html',{'form':form,'elemento':elemento})

@login_required
def atributo_create(request,elemento_id):
    elemento= get_object_or_404(Elemento,pk=elemento_id)
    if request.method=='POST':
        form=AtributoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('elemento_list')
    else:
        form = AtributoForm(initial={'elemento': elemento})
        form.fields['elemento'].widget = forms.HiddenInput()
    return render(request,'atributo/create.html',{'form':form,'elemento':elemento})

@login_required
def atributo_update(request,atributo_id):
    atributo=get_object_or_404(Atributo,pk=atributo_id)
    if request.method=='POST':
        form=AtributoForm(request.POST,instance=atributo)
        if form.is_valid():
            form.save()
            return redirect('elemento_list')
        
    else:
        form=AtributoForm(instance=atributo)

    return render(request,'atributo/update.html',{'form':form,'atributo':atributo})

@login_required
def atributo_delete(request, atributo_id):
    # Obtener el elemento a eliminar
    atributo = get_object_or_404(Atributo, pk=atributo_id)

    if request.method == 'POST':
        atributo.delete()
        return redirect('elemento_list')
    else:
        return render(request, 'atributo/confirm_delete.html', {'atributo': atributo})
    
@login_required
def vulnerabilidad_list(request):
    vulnerabilidades=Vulnerabilidad.objects.all().order_by('valor')
    return render(request,'vulnerabilidad/list.html',{'vulnerabilidades':vulnerabilidades})

@login_required
def vulnerabilidad_create(request):
    if request.method=='POST':
        form=VulnerabilidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vulnerabilidad_list')      
    else:
        form=VulnerabilidadForm()
        return render(request,'vulnerabilidad/create.html',{'form':form})
    

@login_required
def vulnerabilidad_update(request,vulnerabilidad_id):
    vulnerabilidad=get_object_or_404(Vulnerabilidad,pk=vulnerabilidad_id)
    if request.method=='POST':
        form = VulnerabilidadForm(request.POST,instance=vulnerabilidad)
        if form.is_valid():
            form.save()
            return redirect('vulnerabilidad_list')
    else:
        form=VulnerabilidadForm(instance=vulnerabilidad)
        return render(request,'vulnerabilidad/update.html',{'form':form,'vulnerabilidad':vulnerabilidad})


@login_required
def vulnerabilidad_delete(request,vulnerabilidad_id):
    vulnerabilidad=get_object_or_404(Vulnerabilidad,pk=vulnerabilidad_id)
    if request.method=='POST':
        vulnerabilidad.delete()
        return redirect('vulnerabilidad_list')
    else:
        return render(request,'vulnerabilidad/confirm_delete.html',{'vulnerabilidad':vulnerabilidad})

@login_required
def inspector_list(request):
    inspectores=Inspector.objects.all()
    return render(request,'inspector/list.html',{'inspectores':inspectores})

@login_required
def inspector_create(request):
    if request.method == 'POST':
        form = InspectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inspector_list')
        else:
            errors = form.errors.values()
            return render(request, 'inspector/create.html', {'form': form,'errors':errors})
    else:
        form = InspectorForm()
        return render(request, 'inspector/create.html', {'form': form})
    
@login_required
def inspector_update(request,inspector_id):
    inspector=get_object_or_404(Inspector,pk=inspector_id)
    if request.method=='POST':
        form=InspectorForm(request.POST,instance=inspector)
        if form.is_valid():
            form.save()
            return redirect('inspector_list')
    else:
        form=InspectorForm(instance=inspector)
        return render(request,'inspector/update.html',{'form':form,'inspector':inspector})
    
@login_required
def inspector_delete(request,inspector_id):
    inspector=get_object_or_404(Inspector,pk=inspector_id)
    if request.method=='POST':
        inspector.delete()
        return redirect('inspector_list')
    else:
        return render(request,'inspector/confirm_delete.html',{'inspector':inspector})
    
@login_required
def mododefalla_list(request):
    modosdefalla=ModoDeFalla.objects.all().order_by('nombre')
    return render(request,'mododefalla/list.html',{'modosdefalla':modosdefalla})

@login_required
def mododefalla_create(request):
    if request.method=='POST':
        form=ModoDeFallaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mododefalla_list')
        else:
            form=ModoDeFallaForm(request.POST)
            return render(request,'mododefalla/create.html',{'form':form})
    else:
        form=ModoDeFallaForm()
        return render(request,'mododefalla/create.html',{'form':form})
    
@login_required
def mododefalla_update(request,mododefalla_id):
    mododefalla=get_object_or_404(ModoDeFalla,pk=mododefalla_id)
    if request.method=='POST':
        form=ModoDeFallaForm(request.POST,instance=mododefalla)
        if form.is_valid():
            form.save()
            return redirect('mododefalla_list')
        
    else:
        form=ModoDeFallaForm(instance=mododefalla)
        return render(request,'mododefalla/update.html',{'form':form,'mododefalla':mododefalla})
    
@login_required
def mododefalla_delete(request,mododefalla_id):
    mododefalla=get_object_or_404(ModoDeFalla,pk=mododefalla_id)
    if request.method=='POST':
        mododefalla.delete()
        return redirect('mododefalla_list')
    else:
        return render(request,'mododefalla/confirm_delete.html',{'mododefalla':mododefalla})
    
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
        inspeccionform.fields['atributo'].queryset = Atributo.objects.all().order_by('tag')
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
        form = InspeccionForm(instance=inspeccion,initial={'fecha': inspeccion_fecha_iso8601})
        fotoform = FotoForm()
        # Obtener todas las fotos relacionadas con la inspección existente
        fotos = inspeccion.fotos.all()
        # Puedes agregar esta línea si deseas ordenar los atributos por tag en el formulario
        form.fields['atributo'].queryset = Atributo.objects.all().order_by('tag')


    return render(request, 'inspeccion/update.html', {'form': form, 'inspeccion': inspeccion, 'fotoform': fotoform, 'fotos': fotos,'inspeccion_fecha_iso8601':inspeccion_fecha_iso8601})

@login_required
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
    # Obtener la fecha más reciente de cada atributo
    fechas_maximas = Inspeccion.objects.values('atributo').annotate(max_fecha=Max('fecha'))

    # Filtrar las inspecciones que coincidan con las fechas máximas por atributo
    ultimas_inspecciones = Inspeccion.objects.filter(atributo__in=fechas_maximas.values('atributo'), fecha__in=fechas_maximas.values('max_fecha')).order_by('-fecha')

    return render(request, 'inspeccion/ultimas_inspecciones.html', {'ultimas_inspecciones': ultimas_inspecciones})

@login_required
def dashboard(request):
    # Número total de inspecciones realizadas
    total_inspecciones = Inspeccion.objects.count()

    # Distribución de inspecciones por inspector
    inspecciones_por_inspector = Inspeccion.objects.values('inspector__nombre').annotate(total=Count('id'))

    # Distribución de inspecciones por elemento y atributo
    inspecciones_por_elemento_atributo = Inspeccion.objects.values('atributo__elemento__nombre', 'atributo__nombre').annotate(total=Count('id'))

    # Temperatura y vibración promedio por atributo
    # Temperatura y vibración promedio por atributo
    promedio_temperatura_por_atributo = (
        Inspeccion.objects.values('atributo__nombre')
        .annotate(promedio_temperatura=Avg('temperatura'))
    )
    promedio_vibracion_por_atributo = (
        Inspeccion.objects.values('atributo__nombre')
        .annotate(promedio_vibracion=Avg('vibracion'))
    )

    # Modos de falla más comunes
    modos_de_falla_comunes = ModoDeFalla.objects.annotate(total=Count('inspecciones')).order_by('-total')[:5]

    return render(request, 'dashboard/dashboard.html', {
        'total_inspecciones': total_inspecciones,
        'inspecciones_por_inspector': inspecciones_por_inspector,
        'inspecciones_por_elemento_atributo': inspecciones_por_elemento_atributo,
        'promedio_temperatura_por_atributo': promedio_temperatura_por_atributo,
        'promedio_vibracion_por_atributo': promedio_vibracion_por_atributo,
        'modos_de_falla_comunes': modos_de_falla_comunes
    })


def error_404(request, exception):
    return render(request, 'sinpermisos.html', status=404)