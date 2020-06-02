from django.shortcuts import render
import requests
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from amadeus import Client, ResponseError
from .forms import GetHotelDetails
from .models import HotelDetails, ApiReturnList, PnrConfirmedList

# Amadeus connection details - Secret ID for API call
amadeus = Client(
    client_id='lyGlZsuM3AYGJekRlBBjQzMxTahDnyjq',
    client_secret='3lZKe6auNLEUXrTq'
)

def hotels_home(request):
    print('API CALL in hotels_home.html ' + request.method)
    error_code = ' '
    if request.method == "POST":
        form = GetHotelDetails(request.POST)
        if form.is_valid():
            cityname = form.cleaned_data["entercity"]
            checkindate = form.cleaned_data["checkindate"]
            checkoutdate = form.cleaned_data["checkoutdate"]
            adultcount = form.cleaned_data["adultcount"]
            childcount = form.cleaned_data["childcount"]
            roomcount = form.cleaned_data["roomcount"]

            today_date = datetime.date(datetime.now())
            print(today_date)
            if checkindate < today_date:
                error_code = 'checkindatepassed'
            if checkoutdate < today_date:
                error_code = 'checkoutdatepassed'
            if checkoutdate < checkindate:
                error_code = 'checkoutdateinvalid'

            print(cityname)
            if error_code == ' ':
                resp = amadeus.shopping.hotel_offers.get(cityCode=cityname)
                hotels = resp.data
                if len(hotels) == 0:
                    error_code = 'emptyhotellist'

            print("Error code", error_code)

            hotel_list = []
            if error_code == ' ':
                for i in range(len(hotels)):
                    img_suffix = str(i % 6)

                    print("Hotel details for ", i)
                    hotel_data = HotelDetails()
                    hotel_data.hotel_name = hotels[i]['hotel']['name']
                    hotel_data.hotel_id = hotels[i]['hotel']['hotelId']
                    hotel_data.hotel_street = hotels[i]['hotel']['address']['lines'][0]
                    hotel_data.hotel_city = hotels[i]['hotel']['address']['cityName']
                    hotel_data.hotel_state = hotels[i]['hotel']['address']['stateCode']
                    hotel_data.hotel_country = hotels[i]['hotel']['address']['countryCode']
                    hotel_data.hotel_zip = hotels[i]['hotel']['address']['postalCode']
                    hotel_data.hotel_curr  = hotels[i]['offers'][0]['price']['currency']
                    hotel_data.hotel_amt   = hotels[i]['offers'][0]['price']['total']
                    hotel_data.hotel_pic = "rooms/room" + img_suffix + ".jpg"
                    hotel_list.append(hotel_data)

                    # add records to database
                    hotel_insert = ApiReturnList()
                    hotel_insert.hotel_name = hotels[i]['hotel']['name']
                    hotel_insert.hotel_destination_code = cityname
                    hotel_insert.hotel_id = hotels[i]['hotel']['hotelId']
                    hotel_insert.hotel_street1 = hotels[i]['hotel']['address']['lines'][0]
                    hotel_insert.hotel_city = hotels[i]['hotel']['address']['cityName']
                    hotel_insert.hotel_state = hotels[i]['hotel']['address']['stateCode']
                    hotel_insert.hotel_country = hotels[i]['hotel']['address']['countryCode']
                    hotel_insert.hotel_zip = hotels[i]['hotel']['address']['postalCode']
                    hotel_insert.hotel_curr = hotels[i]['offers'][0]['price']['currency']
                    hotel_insert.hotel_amt = hotels[i]['offers'][0]['price']['total']
                    hotel_insert.hotel_inserted = datetime.now()
                    hotel_insert.hotel_pic = "rooms/room" + img_suffix + ".jpg"
                    hotel_insert.save()

        return render(request, "hotels/hotels_home.html", {'form': form, 'hotellist': hotel_list, 'errorcode': error_code})
    else:
        form = GetHotelDetails()
        return render(request, "hotels/hotels_home.html", {'form': form})

def hotels_reserve(request):
    return render(request, "hotels/hotels_reserve.html")

def hotels_history(request):
    pnr_list = PnrConfirmedList.objects.all()
    return render(request, "hotels/hotels_history.html",{'pnrlist': pnr_list})

def hotels_about(request):
    return render(request, "hotels/hotels_about.html")

def hotels_contact(request):
    return render(request, "hotels/hotels_contact.html")

def hotels_placeholder(request):
    return render(request, "hotels/hotels_placeholder.html")

def hotels_mainindex(request):
    return render(request, "users/index.html")


