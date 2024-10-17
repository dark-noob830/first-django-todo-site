from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import UserRegisterForm, UserLoginForm


def register_accounts(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            messages.success(request, "user register successfully.", 'success')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def login_accounts(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, "login successfully.", 'success')
                return redirect('home')
            else:
                messages.error(request, "username or password is not correct.", 'danger')

    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


# Create your views here.
def logout_accounts(request):
    logout(request)
    messages.success(request, "logout successfully.", 'success')
    return redirect('home')
