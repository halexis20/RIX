from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ..models import Inspector
from ..forms import InspectorForm
from .utils import admin_required, render_template

@admin_required
def inspector_list(request):
    inspectores = Inspector.objects.all()
    return render_template(request, 'inspector/list.html', {'inspectores': inspectores})

@admin_required
def inspector_create(request):
    if request.method == 'POST':
        form = InspectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inspector_list')
    else:
        form = InspectorForm()
    return render_template(request, 'inspector/create.html', {'form': form})

@admin_required
def inspector_update(request, inspector_id):
    inspector = get_object_or_404(Inspector, pk=inspector_id)
    if request.method == 'POST':
        form = InspectorForm(request.POST, instance=inspector)
        if form.is_valid():
            form.save()
            return redirect('inspector_list')
    else:
        form = InspectorForm(instance=inspector)
    return render_template(request, 'inspector/update.html', {'form': form, 'inspector': inspector})

@admin_required
def inspector_delete(request, inspector_id):
    inspector = get_object_or_404(Inspector, pk=inspector_id)
    if request.method == 'POST':
        inspector.delete()
        return redirect('inspector_list')
    return render_template(request, 'inspector/confirm_delete.html', {'inspector': inspector})