from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .forms import SignUpForm

import logging

logger = logging.getLogger(__name__)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            messages.add_message(request, messages.ERROR,
                                 'Problem creating your account.')
            return render(request, 'auth/signup.html', {'form': form})
        else:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password)
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.add_message(request, messages.SUCCESS,
                                 'Your account was successfully created.')
            return redirect(reverse('home'))
    else:
        form = SignUpForm()
        return render(request, 'auth/signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('home'))
        else:
            messages.add_message(request, messages.ERROR,
                                 'Username or password invalid')
            return render(request, 'auth/signin.html')
    else:
        return render(request, 'auth/signin.html')


def signout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Successfully signed out.')
    return redirect(reverse('home'))
