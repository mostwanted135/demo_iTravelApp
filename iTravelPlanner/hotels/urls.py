from django.urls import path
from .views import hotels_home

urlpatterns = [
    path('', hotels_home, name='hotels-home'),
]