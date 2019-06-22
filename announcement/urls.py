from django.urls import path, re_path
from announcement.views import *

app_name = 'post'

urlpatterns = [
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
]