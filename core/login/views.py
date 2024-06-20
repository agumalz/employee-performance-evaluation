from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User  

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
        
            if password == confirm_password:
                User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, 'Register Berhasil, Silahkan Login')
                return redirect('login')  # Mengarahkan ke halaman login setelah pendaftaran berhasil
            else:
                messages.error(request, 'Password dan Konfirmasi Password Tidak Sesuai')
        else:
            messages.error(request, 'Form tidak valid. Silakan periksa kembali input Anda.')
            
        return render(request, 'register.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Mengarahkan ke view dashboard
            else:
                messages.error(request, 'Username atau password salah. Silakan coba lagi.')
        else:
            messages.error(request, 'Form tidak valid. Silakan periksa kembali input Anda.')
        
        return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')
