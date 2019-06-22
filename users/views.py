from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render

# from users.forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post:post_create_url')
    else:
        form = UserCreationForm()

    return render(request, 'users/registration.html', {'form': form})
