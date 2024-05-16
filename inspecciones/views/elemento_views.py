from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from ..models import Elemento
from ..forms import ElementoForm
from .utils import admin_required, render_template

@admin_required
def elemento_list(request):
    elementos = Elemento.objects.all().order_by('nombre')
    return render_template(request, 'elemento/list.html', {'elementos': elementos})

@admin_required
def elemento_create(request, elemento_id):
    elemento = get_object_or_404(Elemento, pk=elemento_id)
    if request.method == 'POST':
        form = ElementoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('elemento_list')
    else:
        form = ElementoForm(initial={'padre': elemento})
        form.fields['padre'].widget = forms.HiddenInput()
    return render_template(request, 'elemento/create2.html', {'form': form, 'elemento': elemento})

@admin_required
def elemento_create_base(request):
    if request.method == 'POST':
        form = ElementoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('elemento_list')
    else:
        form = ElementoForm()
    return render_template(request, 'elemento/create.html', {'form': form})

@admin_required
def elemento_update(request, elemento_id):
    elemento = get_object_or_404(Elemento, pk=elemento_id)
    if request.method == 'POST':
        form = ElementoForm(request.POST, instance=elemento)
        if form.is_valid():
            form.save()
            return redirect('elemento_list')
    else:
        form = ElementoForm(instance=elemento)
    return render_template(request, 'elemento/update.html', {'form': form, 'elemento': elemento})

@admin_required
def elemento_delete(request, elemento_id):
    elemento = get_object_or_404(Elemento, pk=elemento_id)
    if request.method == 'POST':
        elemento.delete()
        return redirect('elemento_list')
    return render_template(request, 'elemento/confirm_delete.html', {'elemento': elemento})
