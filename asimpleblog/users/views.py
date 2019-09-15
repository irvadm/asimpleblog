from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect, get_object_or_404

from .forms import UserForm, ProfileForm, PictureForm
from .models import Profile

import logging

logger = logging.getLogger(__name__)


def user_detail(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    return render(request, 'users/user_detail.html', {'profile': profile})


@login_required
def settings_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your profile was successfully updated.')
            return redirect(reverse('users:user_detail', kwargs={'username': request.user.username}))
        else:
            messages.add_message(request, messages.ERROR,
                                 'Please correct error(s) below.')
            return render(request, 'users/settings_profile.html', {
                'user_form': user_form,
                'profile_form': profile_form
            })
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'users/settings_profile.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })


@login_required
def settings_picture(request):
    profile = request.user.profile
    picture_form = PictureForm(instance=profile)
    return render(
        request,
        'users/settings_picture.html',
        {'picture_form': picture_form}
    )
    # else:
    #     form = PictureForm(request.POST, request.FILES, instance=profile)
    #     if form.is_valid():
    #         form.save()
    #         return redirect(
    #             reverse('users:user_detail', kwargs={
    #                 'username': request.user.username
    #             }))
    #     else:
    #         messages.add_message(request, messages.ERROR,
    #                              'Problem trying to update your profile image.')
    #         return render(
    #             request,
    #             'users/settings_picture.html',
    #             {'picture_form': form}
    #         )


@login_required
def upload_picture(request):
    form = PictureForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect(reverse(
            'users:user_detail', kwargs={'username': request.user.username}
        ))
