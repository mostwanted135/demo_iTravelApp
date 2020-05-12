from django.shortcuts import render

def planner_home(request):
    return render(request, "planner_home.html")