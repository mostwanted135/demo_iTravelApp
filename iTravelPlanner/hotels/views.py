from django.shortcuts import render
import requests
from django.shortcuts import render
from django.http import HttpResponse
from amadeus import Client, ResponseError
from .forms import GetHotelDetails
from .models import HotelDetails

# Amadeus connection details - Secret ID for API call
amadeus = Client(
    client_id='lyGlZsuM3AYGJekRlBBjQzMxTahDnyjq',
    client_secret='3lZKe6auNLEUXrTq'
)

def hotels_home(request):
    print('API CALL in hotels_home.html ' + request.method)
    if request.method == "POST":
        form = GetHotelDetails(request.POST)
        if form.is_valid():
            cityname = form.cleaned_data["entercity"]
            print(cityname)
            resp = amadeus.shopping.hotel_offers.get(cityCode=cityname)
            hotels = resp.data
            hotel_list = []
            for i in range(len(hotels)):
                print("Hotel details for ", i)
                hotel_data = HotelDetails()
                hotel_data.hotel_name  = hotels[i]['hotel']['name']
                hotel_data.hotel_id    = hotels[i]['hotel']['hotelId']
                hotel_data.hotel_addr1 = hotels[i]['hotel']['address']['lines'][0]
                hotel_data.hotel_addr2 = hotels[i]['hotel']['address']['cityName']
                hotel_data.hotel_addr3 = hotels[i]['hotel']['address']['stateCode']
                hotel_data.hotel_addr4 = hotels[i]['hotel']['address']['countryCode']
                hotel_data.hotel_addr5 = hotels[i]['hotel']['address']['postalCode']
                hotel_data.hotel_curr  = hotels[i]['offers'][0]['price']['currency']
                hotel_data.hotel_amt   = hotels[i]['offers'][0]['price']['total']
                hotel_list.append(hotel_data)

        return render(request, "hotels/hotels_home.html", {'form': form, 'hotellist': hotel_list})
    else:
        form = GetHotelDetails()
        return render(request, "hotels/hotels_home.html", {'form': form})

def hotels_reserve(request):
    return render(request, "hotels/hotels_reserve.html")

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


