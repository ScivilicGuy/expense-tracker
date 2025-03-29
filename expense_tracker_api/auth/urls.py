from django.contrib import admin
from django.urls import path 
from auth.views import *
from django.conf import settings 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 

urlpatterns = [
  path('', home, name='home'),
  path('login/', login_page, name='login_page'),
  path('register/', register_page, name='register_page')
]