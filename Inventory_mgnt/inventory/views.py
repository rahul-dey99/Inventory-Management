from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm


def home(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            messages.success(request, "You have Registered successfully. You can login now.")
            return redirect('home')
    else:
        form = RegisterUserForm()
        return render(request, 'home.html', {'form':form})
    return render(request, 'home.html', {})

def inventory_view(request):
    return render(request, 'inventory.html', {})
