from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ..models import Vulnerabilidad
from ..forms import VulnerabilidadForm
from .utils import admin_required, render_template

@admin_required
def vulnerabilidad_list(request):
    vulnerabilidades = Vulnerabilidad.objects.all().order_by('valor')
    return render_template(request, 'vulnerabilidad/list.html', {'vulnerabilidades': vulnerabilidades})

@admin_required
def vulnerabilidad_create(request):
    if request.method == 'POST':
        form = VulnerabilidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vulnerabilidad_list')
    else:
        form = VulnerabilidadForm()
    return render_template(request, 'vulnerabilidad/create.html', {'form': form})

@admin_required
def vulnerabilidad_update(request, vulnerabilidad_id):
    vulnerabilidad = get_object_or_404(Vulnerabilidad, pk=vulnerabilidad_id)
    if request.method == 'POST':
        form = VulnerabilidadForm(request.POST, instance=vulnerabilidad)
        if form.is_valid():
            form.save()
            return redirect('vulnerabilidad_list')
    else:
        form = VulnerabilidadForm(instance=vulnerabilidad)
    return render_template(request, 'vulnerabilidad/update.html', {'form': form, 'vulnerabilidad': vulnerabilidad})

@admin_required
def vulnerabilidad_delete(request, vulnerabilidad_id):
    vulnerabilidad = get_object_or_404(Vulnerabilidad, pk=vulnerabilidad_id)
    if request.method == 'POST':
        vulnerabilidad.delete()
        return redirect('vulnerabilidad_list')
    return render_template(request, 'vulnerabilidad/confirm_delete.html', {'vulnerabilidad': vulnerabilidad})
