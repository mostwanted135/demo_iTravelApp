from django.urls import path
from . import views
from .views import hotels_home, hotels_history, hotels_about, hotels_contact, hotels_placeholder, hotels_mainindex, \
    hotels_reserve

urlpatterns = [
    path('', hotels_home, name='hotels-home'),
    path('history/', hotels_history, name='hotels-history'),
    path('contact/', hotels_contact, name='hotels-contact'),
    path('about/', hotels_about, name='hotels-about'),
    path('reserve/', hotels_reserve, name='hotels-reserve'),
    path('placeholder/', hotels_placeholder, name='hotels-placeholder'),
]
