from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from ..models import Equipo, Componente
from ..forms import ComponenteForm
from .utils import admin_required, render_template
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

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


class ComponenteListView(ListView):
    model = Componente
    template_name = 'componente/list.html'
    context_object_name = 'componentes'

    @method_decorator(admin_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ComponenteCreateView(CreateView):
    model = Componente
    template_name = 'componente/create2.html'
    form_class= ComponenteForm
    success_url = reverse_lazy('componente_list')
    #obtiene id por get
    def get_initial(self):
        initial = super().get_initial()
        equipo_id = self.kwargs.get('equipo_id')
        if equipo_id:
            initial['equipo'] = Equipo.objects.get(pk=equipo_id)
        return initial
    #guarda lo indicado en el formulario
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        equipo_id = self.kwargs.get('equipo_id')
        if equipo_id:
            kwargs['initial']['equipo'] = equipo_id
        return kwargs
    # retorna contexto   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        equipo_id = self.kwargs.get('equipo_id')
        if equipo_id:
            context['equipo'] = Equipo.objects.get(pk=equipo_id)
        return context
    
    @method_decorator(admin_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ComponenteUpdateView(UpdateView):
    model = Componente
    form_class=ComponenteForm 
    template_name = 'componente/update.html'
    success_url = reverse_lazy('componente_list')

    @method_decorator(admin_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ComponenteDeleteView(DeleteView):
    model = Componente
    template_name = 'componente/confirm_delete.html'
    success_url = reverse_lazy('componente_list')

    @method_decorator(admin_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
