from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from django.contrib.auth.models import User as user
from django.urls import reverse_lazy

from .models import User,Cod
# Create your views here.
from django.views.generic import CreateView, UpdateView, DetailView, ListView, View
from .forms import UserForm, CodForm, Feedbackform

from django.core.mail import EmailMessage

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



def RecievedStatus(request,pk):
    user=get_object_or_404(User, pk=pk)
    if(request.method=="POST") and ("Taken" in request.POST):
        user.Status=True
        user.save()
    return reverse_lazy('alldata')

def Codmail(request):
    if request.method == "POST":

        email=EmailMessage('Subject', 'Body', to=["malisettydheeraj@gmail.com"])
        email.send()

    render(HttpResponse("Successful"))

class Feedback(CreateView):
    form_class = Feedbackform
    success_url = reverse_lazy('index')
    template_name = 'Feedback.html'

