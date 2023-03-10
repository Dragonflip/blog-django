from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib import messages
from .forms import ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    context = {
        'form': UserRegisterForm()
    }
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Successfully Created for {username}')
            return redirect('login')

    return render(request, 'users/register.html', context) 


@login_required
def profile(request):
    return render(request,'users/profile.html') 

@login_required
def update_profile(request):
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your Profile was Updated')
            return redirect('profile')

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/update_profile.html', context)
