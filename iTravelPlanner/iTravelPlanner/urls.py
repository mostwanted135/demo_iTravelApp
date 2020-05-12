from django.contrib import admin
from django.urls import path, include
import users.views as user_views

urlpatterns = [
    path('', include('users.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('flights/', include('flights.urls')),
    path('planner/', include('planner.urls')),
    path('hotels/', include('hotels.urls'))
]
