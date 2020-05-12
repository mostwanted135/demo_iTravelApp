from django.shortcuts import render

def hotels_home(request):
    return render(request, "hotels/hotels_home.html")
