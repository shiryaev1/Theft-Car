from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#
# class SignUpForm(UserCreationForm):
#     city = forms.CharField()
#     born = forms.DateField()
#
#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'born',
#             'city',
#             'password1',
#             'password2',
#         )