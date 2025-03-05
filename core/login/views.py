from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.http import HttpResponseForbidden

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            position = form.cleaned_data['position']
            password = form.cleaned_data['password']

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username sudah digunakan.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email sudah digunakan.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                Profile.objects.create(user=user, position=position)
                messages.success(request, 'Registrasi berhasil, silakan login.')
                return redirect('login')
        else:
            messages.error(request, 'Form tidak valid. Silakan periksa kembali input Anda.')
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
                # Redirect berdasarkan posisi pengguna
                if user.profile.position == 'crew':
                    return redirect('data_calculate')
                else:
                    return redirect('dashboard:dashboard')
            else:
                messages.error(request, 'Username atau password salah. Silakan coba lagi.')
        else:
            messages.error(request, 'Form tidak valid. Silakan periksa kembali input Anda.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def manager_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if request.user.profile.position == 'manager':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Anda tidak memiliki akses ke halaman ini.")
    return _wrapped_view_func
