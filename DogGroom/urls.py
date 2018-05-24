"""DogGroom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
     url(r'^$', IndexView.as_view(), name = 'index'),
     url(r'^register/', RegistrationView.as_view(), name = 'register'),
     url(r'^home/', HomeView.as_view(), name = 'home'),
     url(r'^home_adddog_form/', AddDogFormView.as_view(), name = 'home_adddog_form'),
     url(r'^booking_delete_view/', DeleteBookingView.as_view(), name = 'booking_delete_view'),
     url(r'^dog_delete_view/', DeleteDogView.as_view(), name='dog_delete_view'),
     url(r'^fetch_date_view/', FetchDateView.as_view()),
     url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
     url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
     url(r'^profile/$', UserUpdateView.as_view(), name='profile'),
     url(r'^booking_update_view/', BookingUpdateView.as_view(), name='bookingmodify'),
     url(r'^dog_update_view/', DogUpdateView.as_view(), name='dogupdateview'),

]
