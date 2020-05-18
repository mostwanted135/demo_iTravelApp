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
hotels = amadeus.shopping.hotel_offers.get(
        cityCode='SYD')
#print(hotels.data)
print(hotels.data[0]['hotel']['name'])
print(hotels.data[0]['hotel']['rating'])
#hotel_offers = amadeus.shopping.hotel_offers_by_hotel.get(
#       hotelId = 'BWSYD207', checkInDate='2020-10-10', checkOutDate='2020-10-12')
#print(hotel_offers.data)
