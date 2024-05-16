from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from ..models import User,UserProfile
from ..forms import UserForm,UserProfileForm,UserEditForm
from .utils import admin_required,render_template

@login_required
def custom_logout(request):
    logout(request)
    return redirect('login')


@admin_required
def user_create(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            return redirect('usuario_list')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'registration/create.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@admin_required
def user_list(request):
    usuarios=User.objects.all()
    return render(request,'usuario/list.html',{'usuarios':usuarios})
 
    
@admin_required
def user_update(request, user_id):
        user = get_object_or_404(User, pk=user_id)
        user_profile = get_object_or_404(UserProfile, user=user)

        if request.method == 'POST':
            user_form = UserEditForm(request.POST, instance=user)
            profile_form = UserProfileForm(request.POST, instance=user_profile)
            
            if user_form.is_valid() and profile_form.is_valid():
                active_admin_count = UserProfile.objects.filter(role='admin', user__is_active=True).count()

                if active_admin_count == 1 and user.userprofile.role == 'admin' and profile_form.cleaned_data['role']=='user':
                    print("No se puede el ultimo admin")
                    return redirect('usuario_list')
                else:
                    print(profile_form.cleaned_data['role'])
                    user_form.save()
                    profile_form.save()
                    return redirect('usuario_list')
        else:
            user_form = UserEditForm(instance=user)
            profile_form = UserProfileForm(instance=user_profile)

        return render(request, 'usuario/update.html', {
            'user_form': user_form,
            'profile_form': profile_form,
        })
  
    
@admin_required
def user_desactivate(request, user_id):
        user = get_object_or_404(User, pk=user_id)
        user_profile = get_object_or_404(UserProfile, user=user)
        
        if user_profile.role == 'admin' or request.user.id== user_id:
            #messages.error(request, "No se puede desactivar un usuario con rol de administrador.")
            return redirect('usuario_list')
        if user.is_active == True:
            #estado= "Desactivado"
            user.is_active = False
            user.save()
        else:
            #estado= "Activado"
            user.is_active = True
            user.save()
        
        #messages.success(request, f"Usuario {estado} exitosamente.")
        return redirect('usuario_list')
