from django.shortcuts import render,get_object_or_404,redirect
from .models import Elemento,Equipo,Vulnerabilidad,Inspector,ModoDeFalla,Inspeccion,Foto,Componente,FuenteDeVulnerabilidad,UserProfile
from .forms import ElementoForm,EquipoForm,VulnerabilidadForm,InspectorForm,ModoDeFallaForm,InspeccionForm,FotoForm,ComponenteForm,FuenteDeVulnerabilidadForm,UserForm,UserProfileForm,UserEditForm
from django.http import HttpRequest,JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms

import calendar
from datetime import datetime, timedelta

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
    if request.user.userprofile.role == 'admin':
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
    else:
        return redirect('sinpermisos')

@login_required
def elemento_delete(request, elemento_id):
    # Obtener el elemento a eliminar
    if request.user.userprofile.role == 'admin':
        elemento = get_object_or_404(Elemento, pk=elemento_id)

        if request.method == 'POST':
            elemento.delete()
            return redirect('elemento_list')
        else:
            return render(request, 'elemento/confirm_delete.html', {'elemento': elemento})
    else:
        return redirect('sinpermisos')

@login_required
def elemento_create_base(request):
    if request.user.userprofile.role == 'admin':
        elementos=Elemento.objects.all()
        if request.method=='POST':
            form=ElementoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('elemento_list')
        else:
            form=ElementoForm()
        
        return render(request,'elemento/create.html',{'form':form,'elementos':elementos})
    else:
        return redirect('sinpermisos')

@login_required
def elemento_update(request,elemento_id):
    if request.user.userprofile.role == 'admin':
        elemento=get_object_or_404(Elemento,pk=elemento_id)
        if request.method=='POST':
            form=ElementoForm(request.POST,instance=elemento)
            if form.is_valid():
                form.save()
                return redirect('elemento_list')
            
        else:
            form=ElementoForm(instance=elemento)

        return render(request,'elemento/update.html',{'form':form,'elemento':elemento})
    else:
        return redirect('sinpermisos')

@login_required
def equipo_create(request,elemento_id):
    if request.user.userprofile.role == 'admin':
        elemento= get_object_or_404(Elemento,pk=elemento_id)
        if request.method=='POST':
            form=EquipoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('elemento_list')
        else:
            form = EquipoForm(initial={'elemento': elemento})
            form.fields['elemento'].widget = forms.HiddenInput()
        return render(request,'equipo/create.html',{'form':form,'elemento':elemento})
    else:
        return redirect('sinpermisos')
    
@login_required
def componente_create(request,equipo_id):
    if request.user.userprofile.role == 'admin':
        equipo= get_object_or_404(Equipo,pk=equipo_id)
        if request.method=='POST':
            form=ComponenteForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('elemento_list')
        else:
            form = ComponenteForm(initial={'equipo': equipo})
            form.fields['equipo'].widget = forms.HiddenInput()
        return render(request,'componente/create.html',{'form':form,'equipo':equipo})
    else:
        return redirect('sinpermisos')

@login_required
def componente_update(request,componente_id):
    if request.user.userprofile.role == 'admin':
        componente=get_object_or_404(Componente,pk=componente_id)
        if request.method=='POST':
            form=ComponenteForm(request.POST,instance=componente)
            if form.is_valid():
                form.save()
                return redirect('elemento_list')
            
        else:
            form=ComponenteForm(instance=componente)

        return render(request,'componente/update.html',{'form':form,'componente':componente})
    else:
        return redirect('sinpermisos')

@login_required
def componente_delete(request, componente_id):
    if request.user.userprofile.role == 'admin':
        # Obtener el elemento a eliminar
        componente = get_object_or_404(Componente, pk=componente_id)

        if request.method == 'POST':
            componente.delete()
            return redirect('elemento_list')
        else:
            return render(request, 'componente/confirm_delete.html', {'componente': componente})
    return redirect('sinpermisos')

@login_required
def equipo_update(request,equipo_id):
    if request.user.userprofile.role == 'admin':
        equipo=get_object_or_404(Equipo,pk=equipo_id)
        if request.method=='POST':
            form=EquipoForm(request.POST,instance=equipo)
            if form.is_valid():
                form.save()
                return redirect('elemento_list')
            
        else:
            form=EquipoForm(instance=equipo)

        return render(request,'equipo/update.html',{'form':form,'equipo':equipo})
    else:
        return redirect('sinpermisos')

@login_required
def equipo_delete(request, equipo_id):
    if request.user.userprofile.role == 'admin':
        # Obtener el elemento a eliminar
        equipo = get_object_or_404(Equipo, pk=equipo_id)

        if request.method == 'POST':
            equipo.delete()
            return redirect('elemento_list')
        else:
            return render(request, 'equipo/confirm_delete.html', {'equipo': equipo})
    return redirect('sinpermisos')
    
@login_required
def vulnerabilidad_list(request):
    if request.user.userprofile.role == 'admin':
        vulnerabilidades=Vulnerabilidad.objects.all().order_by('valor')
        return render(request,'vulnerabilidad/list.html',{'vulnerabilidades':vulnerabilidades})
    else:
        return redirect('sinpermisos')

@login_required
def vulnerabilidad_create(request):
    if request.user.userprofile.role == 'admin':
        if request.method=='POST':
            form=VulnerabilidadForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('vulnerabilidad_list')      
        else:
            form=VulnerabilidadForm()
            return render(request,'vulnerabilidad/create.html',{'form':form})
    else:
        return redirect('sinpermisos')
    

@login_required
def vulnerabilidad_update(request,vulnerabilidad_id):
    if request.user.userprofile.role == 'admin':
        vulnerabilidad=get_object_or_404(Vulnerabilidad,pk=vulnerabilidad_id)
        if request.method=='POST':
            form = VulnerabilidadForm(request.POST,instance=vulnerabilidad)
            if form.is_valid():
                form.save()
                return redirect('vulnerabilidad_list')
        else:
            form=VulnerabilidadForm(instance=vulnerabilidad)
            return render(request,'vulnerabilidad/update.html',{'form':form,'vulnerabilidad':vulnerabilidad})
    else:
        return redirect('sinpermisos')


@login_required
def vulnerabilidad_delete(request,vulnerabilidad_id):
    if request.user.userprofile.role == 'admin':
        vulnerabilidad=get_object_or_404(Vulnerabilidad,pk=vulnerabilidad_id)
        if request.method=='POST':
            vulnerabilidad.delete()
            return redirect('vulnerabilidad_list')
        else:
            return render(request,'vulnerabilidad/confirm_delete.html',{'vulnerabilidad':vulnerabilidad})
    else:
        return redirect('sinpermisos')

@login_required
def inspector_list(request):
    if request.user.userprofile.role == 'admin':
        inspectores=Inspector.objects.all()
        return render(request,'inspector/list.html',{'inspectores':inspectores})
    else:
        return redirect('sinpermisos')

@login_required
def inspector_create(request):
    if request.user.userprofile.role == 'admin':
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
    else:
        return redirect('sinpermisos')
    
@login_required
def inspector_update(request,inspector_id):
    if request.user.userprofile.role == 'admin':
        inspector=get_object_or_404(Inspector,pk=inspector_id)
        if request.method=='POST':
            form=InspectorForm(request.POST,instance=inspector)
            if form.is_valid():
                form.save()
                return redirect('inspector_list')
        else:
            form=InspectorForm(instance=inspector)
            return render(request,'inspector/update.html',{'form':form,'inspector':inspector})
    else:
        return redirect('sinpermisos')
    
@login_required
def inspector_delete(request,inspector_id):
    if request.user.userprofile.role == 'admin':
        inspector=get_object_or_404(Inspector,pk=inspector_id)
        if request.method=='POST':
            inspector.delete()
            return redirect('inspector_list')
        else:
            return render(request,'inspector/confirm_delete.html',{'inspector':inspector})
    else:
        return redirect('sinpermisos')
    
@login_required
def mododefalla_list(request):
    if request.user.userprofile.role == 'admin':
        modosdefalla=ModoDeFalla.objects.all().order_by('nombre')
        return render(request,'mododefalla/list.html',{'modosdefalla':modosdefalla})
    else:
        return redirect('sinpermisos')

@login_required
def mododefalla_create(request):
    if request.user.userprofile.role == 'admin':
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
    else:
        return redirect('sinpermisos')
    
@login_required
def mododefalla_update(request,mododefalla_id):
    if request.user.userprofile.role == 'admin':
        mododefalla=get_object_or_404(ModoDeFalla,pk=mododefalla_id)
        if request.method=='POST':
            form=ModoDeFallaForm(request.POST,instance=mododefalla)
            if form.is_valid():
                form.save()
                return redirect('mododefalla_list')
            
        else:
            form=ModoDeFallaForm(instance=mododefalla)
            return render(request,'mododefalla/update.html',{'form':form,'mododefalla':mododefalla})
    else:
        return redirect('sinpermisos')
    
@login_required
def mododefalla_delete(request,mododefalla_id):
    if request.user.userprofile.role == 'admin':
        mododefalla=get_object_or_404(ModoDeFalla,pk=mododefalla_id)
        if request.method=='POST':
            mododefalla.delete()
            return redirect('mododefalla_list')
        else:
            return render(request,'mododefalla/confirm_delete.html',{'mododefalla':mododefalla})
    else:
        return redirect('sinpermisos')    
    
    
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

@login_required
def inspeccion_delete(request,inspeccion_id):
    if request.user.userprofile.role == 'admin':
        inspeccion=get_object_or_404(Inspeccion,pk=inspeccion_id)
        if request.method=='POST':
            inspeccion.delete()
            return redirect('inspeccion_list')
        else:
            return render(request,'inspeccion/confirm_delete.html',{'inspeccion':inspeccion})
    else:
        return redirect('sinpermisos')

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


def error_404(request, exception):
    return render(request, 'sinpermisos.html', status=404)


@login_required
def fuentedevulnerabilidad_list(request):
    if request.user.userprofile.role == 'admin':
        fuentesdevulnerabilidad=FuenteDeVulnerabilidad.objects.all()
        return render(request,'fuentedevulnerabilidad/list.html',{'fuentesdevulnerabilidad':fuentesdevulnerabilidad})
    else:
        return redirect('sinpermisos')

@login_required
def fuentedevulnerabilidad_create(request):
    if request.user.userprofile.role == 'admin':
        if request.method=='POST':
            form=FuenteDeVulnerabilidadForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('fuentedevulnerabilidad_list')
            else:
                form=FuenteDeVulnerabilidadForm(request.POST)
                return render(request,'fuentedevulnerabilidad/create.html',{'form':form})
        else:
            form=FuenteDeVulnerabilidadForm()
            return render(request,'fuentedevulnerabilidad/create.html',{'form':form})
    else:
        return redirect('sinpermisos')
    
@login_required
def fuentedevulnerabilidad_update(request,fuentedevulnerabilidad_id):
    if request.user.userprofile.role == 'admin':
        fuentedevulnerabilidad=get_object_or_404(FuenteDeVulnerabilidad,pk=fuentedevulnerabilidad_id)
        if request.method=='POST':
            form=FuenteDeVulnerabilidadForm(request.POST,instance=fuentedevulnerabilidad)
            if form.is_valid():
                form.save()
                return redirect('fuentedevulnerabilidad_list')
            
        else:
            form=FuenteDeVulnerabilidadForm(instance=fuentedevulnerabilidad)
            return render(request,'fuentedevulnerabilidad/update.html',{'form':form,'fuentedevulnerabilidad':fuentedevulnerabilidad})
    else:
        return redirect('sinpermisos')
    
@login_required
def fuentedevulnerabilidad_delete(request,fuentedevulnerabilidad_id):
    if request.user.userprofile.role == 'admin':
        fuentedevulnerabilidad=get_object_or_404(FuenteDeVulnerabilidad,pk=fuentedevulnerabilidad_id)
        if request.method=='POST':
            fuentedevulnerabilidad.delete()
            return redirect('fuentedevulnerabilidad_list')
        else:
            return render(request,'fuentedevulnerabilidad/confirm_delete.html',{'fuentedevulnerabilidad':fuentedevulnerabilidad})
    else:
        return redirect('sinpermisos')  
    

@login_required
def componente_list(request):
    componentes = Componente.objects.all()
    return render(request, 'componente/list.html', {'componentes': componentes})


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

@login_required
def user_create(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            return redirect('inspeccion_list')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'registration/create.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def user_list(request):
    if request.user.userprofile.role == 'admin':
        usuarios=User.objects.all()
        return render(request,'usuario/list.html',{'usuarios':usuarios})
    else:
        return redirect('sinpermisos')    
    
@login_required
def user_update(request, user_id):
    if request.user.userprofile.role == 'admin':
        user = get_object_or_404(User, pk=user_id)
        user_profile = get_object_or_404(UserProfile, user=user)

        if request.method == 'POST':
            user_form = UserEditForm(request.POST, instance=user)
            profile_form = UserProfileForm(request.POST, instance=user_profile)
            
            if user_form.is_valid() and profile_form.is_valid():
                active_admin_count = UserProfile.objects.filter(role='admin', user__is_active=True).count()

                if active_admin_count == 1 and user.userprofile.role == 'admin' and profile_form.cleaned_data['role']=='user':
                    print("No se puede el ultimo admin")
                    return redirect('usuario_list')
                else:
                    print(profile_form.cleaned_data['role'])
                    user_form.save()
                    profile_form.save()
                    return redirect('usuario_list')
        else:
            user_form = UserEditForm(instance=user)
            profile_form = UserProfileForm(instance=user_profile)

        return render(request, 'usuario/update.html', {
            'user_form': user_form,
            'profile_form': profile_form,
        })
    else:
        return redirect('sinpermisos')   
    
@login_required
def user_desactivate(request, user_id):
    if request.user.userprofile.role == 'admin':
        user = get_object_or_404(User, pk=user_id)
        user_profile = get_object_or_404(UserProfile, user=user)
        
        if user_profile.role == 'admin' or request.user.id== user_id:
            #messages.error(request, "No se puede desactivar un usuario con rol de administrador.")
            return redirect('usuario_list')
        if user.is_active == True:
            #estado= "Desactivado"
            user.is_active = False
            user.save()
        else:
            #estado= "Activado"
            user.is_active = True
            user.save()
        
        #messages.success(request, f"Usuario {estado} exitosamente.")
        return redirect('usuario_list')
    else:
        return redirect('sinpermisos')