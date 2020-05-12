from django.urls import path
from .views import flights_home
import django.contrib.auth.views as auth_views

urlpatterns = [
    path('', flights_home, name='flights-home'),
]