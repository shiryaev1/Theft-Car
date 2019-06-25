from django.urls import path, re_path
from announcement.views import *

app_name = 'announcement'

urlpatterns = [
    path('create/', AnnouncementCreate.as_view(),
         name='announcement_create_url'),
    # path('user-page/', user_page, name='user-page'),
    path('', announcement_list, name='announcement-list')
]