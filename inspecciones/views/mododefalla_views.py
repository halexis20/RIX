from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from ..models import ModoDeFalla
from ..forms import ModoDeFallaForm
from .utils import admin_required,render_template


@admin_required
def mododefalla_list(request):
        modosdefalla=ModoDeFalla.objects.all().order_by('nombre')
        return render(request,'mododefalla/list.html',{'modosdefalla':modosdefalla})


@admin_required
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

    
@admin_required
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
    
@admin_required
def mododefalla_delete(request,mododefalla_id):
        mododefalla=get_object_or_404(ModoDeFalla,pk=mododefalla_id)
        if request.method=='POST':
            mododefalla.delete()
            return redirect('mododefalla_list')
        else:
            return render(request,'mododefalla/confirm_delete.html',{'mododefalla':mododefalla})