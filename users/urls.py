from django.contrib.auth.views import LoginView
from django.urls import path, re_path
from users import views
# from users.views import LoginFormView

app_name = 'use'

urlpatterns = [

    path('registration/', views.registration, name='registration'),
    # path('login/', LoginFormView.as_view(), name='login'),
    path('login/', LoginView.as_view(template_name='users/login.html'),
         name='login'),
    re_path(r'^profile/(?P<pk>\d+)/$', views.view_profile,
            name='view_profile_with_pk'),
    path('profile/', views.view_profile, name='view_profile'),
]