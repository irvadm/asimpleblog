from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.http import is_safe_url

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
        redirect_to = request.POST['next']

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if not user:
            messages.add_message(request, messages.ERROR,
                                 'Username or password invalid')
            return render(request, 'auth/signin.html')
        else:
            login(request, user)
            if redirect_to and is_safe_url(redirect_to, allowed_hosts=None):
                logger.info(f'Redirecting to {redirect_to}')
                return redirect(redirect_to)
            return redirect(reverse('home'))
    else:
        return render(request, 'auth/signin.html')


def signout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Successfully signed out.')
    return redirect(reverse('home'))
