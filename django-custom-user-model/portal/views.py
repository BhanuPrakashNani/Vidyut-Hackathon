from django.shortcuts import render
from django.contrib.auth.models import User as user
from django.urls import reverse_lazy

from .models import User,Cod
# Create your views here.
from django.views.generic import CreateView, UpdateView, DetailView, ListView, View
from .forms import UserForm, CodForm

class Userdata(CreateView):
    form_class =UserForm
    success_url = reverse_lazy('home1')
    template_name = 'registration/orderentry.html'

class Alldata(ListView):
    model = User
    template_name = 'registration/Alldata.html'
    queryset = User.objects.order_by('date')
#
# def Personaldata(ListView):
#     model = User
#     template_name = 'registration/Personaldata.html'
#     queryset = User.objects.filter(roll_no=)

class CodData(CreateView):
    form_class= CodForm
    success_url = reverse_lazy('home')
    template_name='registration/CodData.html'


class CodDataNotifications(ListView):
    model = Cod
    template_name = 'registration/CodDataNotifications.html'
    queryset = Cod.objects.order_by('Eta')

def
