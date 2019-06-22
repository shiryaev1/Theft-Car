from django.urls import path
from users import views as s


urlpatterns = [

    path('registration/', s.signup, name='signup'),

]