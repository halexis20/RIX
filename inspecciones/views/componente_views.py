from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from ..models import Equipo, Componente
from ..forms import ComponenteForm
from .utils import admin_required, render_template


@admin_required
def componente_list(request):
    componentes = Componente.objects.all()
    return render(request, 'componente/list.html', {'componentes': componentes})

@admin_required
def componente_create(request, equipo_id):
    equipo = get_object_or_404(Equipo, pk=equipo_id)
    if request.method == 'POST':
        form = ComponenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('elemento_list')
    else:
        form = ComponenteForm(initial={'equipo': equipo})
        form.fields['equipo'].widget = forms.HiddenInput()
    return render_template(request, 'componente/create.html', {'form': form, 'equipo': equipo})

@admin_required
def componente_update(request, componente_id):
    componente = get_object_or_404(Componente, pk=componente_id)
    if request.method == 'POST':
        form = ComponenteForm(request.POST, instance=componente)
        if form.is_valid():
            form.save()
            return redirect('elemento_list')
    else:
        form = ComponenteForm(instance=componente)
    return render_template(request, 'componente/update.html', {'form': form, 'componente': componente})

@admin_required
def componente_delete(request, componente_id):
    componente = get_object_or_404(Componente, pk=componente_id)
    if request.method == 'POST':
        componente.delete()
        return redirect('elemento_list')
    return render_template(request, 'componente/confirm_delete.html', {'componente': componente})
