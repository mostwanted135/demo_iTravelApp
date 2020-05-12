
from django.urls import path, include
from .views import planner_home

urlpatterns = [
    path('',planner_home, name='planner-home'),
]