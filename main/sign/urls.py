from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView
from django.views.decorators.cache import cache_page


app_name = 'sign'


urlpatterns = [
    path('login/',
         cache_page(60*10)(LoginView.as_view(template_name='sign/login.html')),
         name='login'),
    path('logout/',
         cache_page(60*10)(LogoutView.as_view(template_name='sign/logout.html')),
         name='logout'),
    path('signup/',
         cache_page(60*10)(BaseRegisterView.as_view(template_name='sign/signup.html')),
         name='signup'),
]