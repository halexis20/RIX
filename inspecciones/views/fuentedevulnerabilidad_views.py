from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from ..models import FuenteDeVulnerabilidad
from ..forms import FuenteDeVulnerabilidadForm
from .utils import admin_required,render_template


@admin_required
def fuentedevulnerabilidad_list(request):
        fuentesdevulnerabilidad=FuenteDeVulnerabilidad.objects.all()
        return render(request,'fuentedevulnerabilidad/list.html',{'fuentesdevulnerabilidad':fuentesdevulnerabilidad})


@admin_required
def fuentedevulnerabilidad_create(request):
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

    
@admin_required
def fuentedevulnerabilidad_update(request,fuentedevulnerabilidad_id):
        fuentedevulnerabilidad=get_object_or_404(FuenteDeVulnerabilidad,pk=fuentedevulnerabilidad_id)
        if request.method=='POST':
            form=FuenteDeVulnerabilidadForm(request.POST,instance=fuentedevulnerabilidad)
            if form.is_valid():
                form.save()
                return redirect('fuentedevulnerabilidad_list')
            
        else:
            form=FuenteDeVulnerabilidadForm(instance=fuentedevulnerabilidad)
            return render(request,'fuentedevulnerabilidad/update.html',{'form':form,'fuentedevulnerabilidad':fuentedevulnerabilidad})

    
@admin_required
def fuentedevulnerabilidad_delete(request,fuentedevulnerabilidad_id):
        fuentedevulnerabilidad=get_object_or_404(FuenteDeVulnerabilidad,pk=fuentedevulnerabilidad_id)
        if request.method=='POST':
            fuentedevulnerabilidad.delete()
            return redirect('fuentedevulnerabilidad_list')
        else:
            return render(request,'fuentedevulnerabilidad/confirm_delete.html',{'fuentedevulnerabilidad':fuentedevulnerabilidad})
