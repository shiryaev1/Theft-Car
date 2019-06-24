
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login
from django.template.context_processors import csrf
from django.views.generic import FormView
from django.views.generic.base import View

from announcement.models import Announcement


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('announcement:announcement_create_url')
    else:
        form = UserCreationForm()

    return render(request, 'users/registration.html', {'form': form})


# class LoginFormView(FormView):
#     form_class = AuthenticationForm
#
#     template_name = "users/login.html"
#
#     success_url = ''
#
#     def form_valid(self, form):
#         self.user = form.get_user()
#
#         csrf(login(self.request, self.user))
#         return super(LoginFormView, self).form_valid(form)


def view_profile(request, pk=None):
    users = None
    if pk:
        if int(pk) == request.user.id:
            return redirect('accounts:view_profile')
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
        'post': user_post,
        'post_last': results,
        'users': users,


    }

    return render(request, 'users/user_page.html', args)
