from django.shortcuts import render

def planner_home(request):
    return render(request, "planner/planner_home.html")