from django.shortcuts import render,redirect
from django.http import HttpResponseForbidden
from functools import wraps

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.userprofile.role == 'admin':
            return redirect('sinpermisos')   
            #return HttpResponseForbidden("No tiene permisos para acceder a esta página.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def render_template(request, template_name, context=None):
    return render(request, template_name, context)

def error_404(request, exception):
    return render(request, 'sinpermisos.html', status=404)

def sin_permisos(request):
    
    return render(request,'sinpermisos.html',{})  