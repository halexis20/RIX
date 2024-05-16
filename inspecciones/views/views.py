from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def sin_permisos(request):
    
    return render(request,'sinpermisos.html',{})  
  
