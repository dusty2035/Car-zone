from django.shortcuts import render
from .models import Team
from cars.models import Car
# Create your views here.

def home(request):
    team = Team.objects.all
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    data = {
        'teams' : team ,
        'featured_cars' : featured_cars ,
    }
    return render(request, 'pages/home.html' , data)


def about(request):
    team = Team.objects.all
    return render(request, 'pages/about.html' , { 'teams' : team })


def services(request):
    return render(request , 'pages/services.html')


def contact(request):
    return render(request , 'pages/contact.html')