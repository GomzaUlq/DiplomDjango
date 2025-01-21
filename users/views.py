from django.shortcuts import render, redirect
from .forms import Registration, Login
from django.contrib.auth import login, authenticate, logout

from .models import Profile


def registration(request):
    info_error = {}
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 == password2:
                existing_users = Profile.objects.filter(username=username) | Profile.objects.filter(email=email)
                if existing_users.exists():
                    info_error['error'] = 'Пользователь с таким именем или email уже существует'
                else:
                    user = form.save(commit=False)
                    user.set_password(form.cleaned_data['password1'])
                    user.save()
                    return redirect('login')
            else:
                info_error['error'] = 'Пароли не совпадают'
    else:
        form = Registration()
    return render(request, 'users/registrarion_page.html', {'form': form, 'info_error': info_error})


def login_up(request):
    info_error = {}
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                info_error['error'] = 'Неверный логин или пароль'
    else:
        form = Login()
    return render(request, 'users/login.html', {'form': form, 'info_error': info_error})


def log_out(request):
    logout(request)
    return redirect('login')
