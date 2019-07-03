
from datetime import datetime, timedelta

from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render, render_to_response
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login
from django.template.context_processors import csrf
from django.views.generic import FormView
from django.views.generic.base import View

from announcement.models import Announcement
from users.forms import RegistrationForm

from .forms import UploadPhotoForm

# Imaginary function to handle an uploaded file.


class UploadPhoto(View):
    def get(self,request, pk):
        profile = User.objects.get(pk=pk)
        upload_form = UploadPhotoForm()
        context = {'form': upload_form, 'profile': profile}
        return render(request, 'users/upload_photo.html', context)

    def post(self,request, pk):
        profile = User.objects.get(pk=pk)
        edit_bount_form = UploadPhotoForm(request.POST or None,
                                          request.FILES,
                                          )
        if edit_bount_form.is_valid():
            if 'image' in request.FILES:
                edit_bount_form.image = request.FILES['image']
            edit_bount_form.save(request.user)
            return redirect('use:view_profile')
        else:
            print(edit_bount_form.errors)
        context = {'form': edit_bount_form}
        return render(request, 'users/upload_photo.html', context)


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('announcement:announcement_create_url')
    else:
        form = RegistrationForm()

    return render(request, 'users/registration.html', {'form': form})


def view_profile(request, pk=None):
    users = None
    if pk:
        if int(pk) == request.user.id:
            return redirect('use:view_profile')
        user = User.objects.get(pk=pk)
        user_post = Announcement.objects.filter(author_id=int(pk)).order_by('-created')
        last_minute = datetime.now(tz=timezone.utc) - timedelta(1)
        results = Announcement.objects.filter(created__gt=last_minute)

    else:
        user = request.user
        user_post = Announcement.objects.filter(author_id=user.id).order_by('-created')
        last_minute = datetime.now(tz=timezone.utc) - timedelta(1)
        results = Announcement.objects.filter(created__gt=last_minute).last()
        users = User.objects.exclude(id=request.user.id)

    args = {
        'user': user,
        'announcements': user_post,
        'post_last': results,
        'users': users,


    }

    return render(request, 'users/user_page.html', args)
