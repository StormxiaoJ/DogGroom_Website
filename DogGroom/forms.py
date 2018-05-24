from django import forms
from .models import Dog, Appointment
from .const import *
# form for creating an appointment

class NewAppointmentForm(forms.ModelForm):

    date = forms.DateField(widget=forms.DateInput(attrs={'id': 'selectdate'}))
    starttime = forms.CharField(widget=forms.Select(attrs={'id': 'selecttime'}))
    class Meta:
        model = Appointment
        fields = ['dog', 'washoption', 'date', 'starttime', 'instruction']

class UpdateAppointmentForm(forms.ModelForm):


    date = forms.DateField(widget=forms.DateInput(attrs={'id': 'selectdate_for_modify'}))
    # starttime = forms.CharField(widget=forms.Select(attrs={'id': 'selecttime_for_update'}))
    # starttime = forms.ChoiceField(choices = daytime_slots_choices)
    starttime = forms.CharField(widget=forms.Select(attrs={'id': 'selecttime_for_modify'}))
    class Meta:
        model = Appointment
        fields = ['dog', 'washoption', 'date', 'starttime', 'instruction']


class NewDogForm(forms.ModelForm):

    dob = forms.DateField(widget=forms.SelectDateWidget(years=range(1990, 2019), attrs={'id': 'selectdate'}))
    class Meta:
        model = Dog
        fields = ['dogname', 'breed', 'dob']