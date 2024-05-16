from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from ..models import Elemento, Equipo
from ..forms import EquipoForm
from .utils import admin_required, render_template

@admin_required
def equipo_create(request, elemento_id):
    elemento = get_object_or_404(Elemento, pk=elemento_id)
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('elemento_list')
    else:
        form = EquipoForm(initial={'elemento': elemento})
        form.fields['elemento'].widget = forms.HiddenInput()
    return render_template(request, 'equipo/create.html', {'form': form, 'elemento': elemento})

@admin_required
def equipo_update(request, equipo_id):
    equipo = get_object_or_404(Equipo, pk=equipo_id)
    if request.method == 'POST':
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('elemento_list')
    else:
        form = EquipoForm(instance=equipo)
    return render_template(request, 'equipo/update.html', {'form': form, 'equipo': equipo})

@admin_required
def equipo_delete(request, equipo_id):
    equipo = get_object_or_404(Equipo, pk=equipo_id)
    if request.method == 'POST':
        equipo.delete()
        return redirect('elemento_list')
    return render_template(request, 'equipo/confirm_delete.html', {'equipo': equipo})
