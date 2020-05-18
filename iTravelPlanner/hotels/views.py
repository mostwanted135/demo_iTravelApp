from django.shortcuts import render
import requests
from django.shortcuts import render
from django.http import HttpResponse
from amadeus import Client, ResponseError

# Amadeus connection details - Secret ID for API call
amadeus = Client(
    client_id='lyGlZsuM3AYGJekRlBBjQzMxTahDnyjq',
    client_secret='3lZKe6auNLEUXrTq'
)

def hotels_home(request):
    return render(request, "hotels/hotels_home.html")

def hotels_history(request):
    return render(request, "hotels/hotels_history.html")

def hotels_about(request):
    return render(request, "hotels/hotels_about.html")

def hotels_contact(request):
    return render(request, "hotels/hotels_contact.html")

def hotels_placeholder(request):
    return render(request, "hotels/hotels_placeholder.html")

def hotels_mainindex(request):
    return render(request, "users/index.html")

# request   city, count
# response  hotel details
def hotels_api_gethotel_sendcitycount(request):
    searchcity = request.GET.get('searchcity')
    resp = amadeus.shopping.hotel_offers.get(
        cityCode='SYD',
        adults=1,
        radius=5,
        radiusunit='KM'
    )

