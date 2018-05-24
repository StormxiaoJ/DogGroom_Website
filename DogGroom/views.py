from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from Account.forms import *
from .models import *
from .forms import *
from .ScheduleController import *
import json

from django.core.mail import send_mail

# Create your views here.

# class-based view
class IndexView(View):

    def get(self, request):
        if (request.user.is_authenticated):
            return redirect('home')
        else:
            return render(request, 'index.html')

class HomeView(LoginRequiredMixin, View):

    login_url = '/'
    
    def get(self, request):
        dogs = Dog.objects.filter(owner = request.user)
        bookings = Appointment.objects.filter(client = request.user)
        
        booking_form = NewAppointmentForm()
        booking_form.fields['dog'].queryset = dogs
        
        adddog_form = NewDogForm()
        
        return render(request, 'home.html',
                      {'mydogs': dogs, 
                       'mybookings': bookings, 
                       'booking_form': booking_form, 
                       'adddog_form': adddog_form})

    def post(self, request):

        booking = Appointment(client = request.user)
        booking_form = NewAppointmentForm(request.POST, instance = booking)

        if booking_form.is_valid():
            booking_form.save()
            return redirect('home')
        else:
            return HttpResponse(booking_form.errors)

class AddDogFormView(LoginRequiredMixin, View):

    def get(self, request):
        return redirect('home')

    def post(self, request):
        dog = Dog(owner = request.user)
        adddog_form = NewDogForm(request.POST, instance = dog)
        if adddog_form.is_valid():
            adddog_form.save()
            return redirect('home')
        else:
            # return HttpResponse(booking_form.errors)
            return render(request, 'formatmessage.html')

class FetchDateView(View):

    def get(self, request):
        return redirect('home')
    
    def post(self, request):
        selecteddate = request.POST.get('selectdate')
        sc = ScheduleController()
        slotlist = sc.get_availableslot(selecteddate)
        data = {"list_of_avail" : slotlist}
        return HttpResponse(json.dumps(data), content_type='application/json')

class DeleteBookingView(LoginRequiredMixin, View):
    
    def get(self, request):
        return redirect('home')

    def post(self, request):
        
        id_list = request.POST.getlist('id_list')
        
        for id_ in id_list:
            Appointment.objects.filter(bookingid = id_).delete()
        return redirect('home')

class DeleteDogView(LoginRequiredMixin, View):
    
    def get(self, request):
        return redirect('home')

    def post(self, request):
        
        id_list = request.POST.getlist('id_list')
        
        for id_ in id_list:
            Dog.objects.filter(dogid = id_).delete()
        return redirect('home')



class RegistrationView(View):

    def get(self, request):
        form = UserAdminCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # save the users to database
            auth_login(request, user) # log him/her in
            return redirect('home')
        else:
            return HttpResponse(form.errors)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'
    model = User
    fields = ('first_name', 'last_name', 'email', 
              'address', 'phone_mobile', 'phone_home', 
              'phone_work')
    template_name = 'profile.html'
    success_url = reverse_lazy('home')

    def get(self, request, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        userform = self.get_form(form_class)
        context = self.get_context_data(object = self.object, form = userform)
        return self.render_to_response(context)

    def get_object(self):
        return self.request.user

class BookingUpdateView(UpdateView):
    # login_url = '/'
    model = Appointment
    fields = ('dog', 'date', 'starttime', 
              'washoption', 'instruction')
              
    template_name = 'bookingprofile.html'
    success_url = reverse_lazy('home')

    def get(self, request, **kwargs):

        dogs = Dog.objects.filter(owner = request.user)
        booking_form = UpdateAppointmentForm()
        # booking_form.fields['dog'].queryset = dogs

        self.object = self.get_object()
        currentdate = self.object.date
        # form_class = self.get_form_class()
        form_class = UpdateAppointmentForm
        apptform = self.get_form(form_class)
        apptform.fields['dog'].queryset = dogs
        context = self.get_context_data(object = self.object, form = apptform)
        return self.render_to_response(context)

    def get_object(self):
        id = self.request.GET.get('tobemodified')
        appt =  self.model.objects.get(bookingid=id)
        # Appointment.objects.get(bookingid=id).delete()
        
        return appt

class DogUpdateView(UpdateView):

    model = Dog
    fields = ('dogname', 'dob', 'breed')
    template_name = 'profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        id = self.request.GET.get('dogtobemodified')
        dog =  self.model.objects.get(dogid=id)
        return dog

    def get(self, request, **kwargs):
        self.object = self.get_object()
        print(self.object)
        form_class = self.get_form_class()
        dogform = self.get_form(form_class)
        context = self.get_context_data(object = self.object, form = dogform)
        return self.render_to_response(context)