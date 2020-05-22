from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from amadeus import Client, ResponseError

# Amadeus connection details - Secret ID for API call
amadeus = Client(
    client_id='lyGlZsuM3AYGJekRlBBjQzMxTahDnyjq',
    client_secret='3lZKe6auNLEUXrTq'
)
resp = amadeus.shopping.hotel_offers.get(
        cityCode='SYD')
hotels = resp.data
for i in range(6):
    hotel_name = hotels[i]['hotel']['name']
    hotel_id = hotels[i]['hotel']['hotelId']
    hotel_addr1 = hotels[i]['hotel']['address']['lines'][0]
    hotel_addr2 = hotels[i]['hotel']['address']['cityName']
    hotel_addr3 = hotels[i]['hotel']['address']['stateCode']
    hotel_addr4 = hotels[i]['hotel']['address']['countryCode']
    hotel_addr5 = hotels[i]['hotel']['address']['postalCode']
    hotel_curr = hotels[i]['offers'][0]['price']['currency']
    hotel_amt  = hotels[i]['offers'][0]['price']['total']
    print(hotel_name)
    print(hotel_id)
    print(hotel_addr1)
    print(hotel_addr2)
    print(hotel_addr3)
    print(hotel_addr4)
    print(hotel_addr5)
    print(hotel_curr)
    print(hotel_amt)
#hotel_offers = amadeus.shopping.hotel_offers_by_hotel.get(
#       hotelId = 'BWSYD207', checkInDate='2020-10-10', checkOutDate='2020-10-12')
#print(hotel_offers.data)