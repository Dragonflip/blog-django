from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib import messages


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

def profile(request):
    return render(request,'users/profile.html') 
