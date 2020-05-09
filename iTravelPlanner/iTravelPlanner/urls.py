from django.contrib import admin
from django.urls import path
import django.contrib.auth.views as auth_views
import users.views as user_views


urlpatterns = [
    path('', user_views.home, name='users-home'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='users-logout'),
    path('register/', user_views.createUser, name='users-register')
]
