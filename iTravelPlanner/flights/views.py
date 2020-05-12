from django.shortcuts import render

def flights_home(request):
    return render(request, "flights/flights_home.html")
