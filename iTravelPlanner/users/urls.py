from django.urls import path
from .views import home, createUser
import django.contrib.auth.views as auth_views

urlpatterns = [
    path('', home, name='users-home'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='users-logout'),
    path('register/', createUser, name='users-register')
 
]