from django.shortcuts import render
from .models import Team
from cars.models import Car
# Create your views here.

def home(request):
    team = Team.objects.all
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    # returns List 
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'teams' : team ,
        'featured_cars' : featured_cars ,
        'model_search' : model_search ,
        'city_search' : city_search ,
        'year_search' : year_search ,
        'body_style_search' : body_style_search ,

    }
    return render(request, 'pages/home.html' , data)


def about(request):
    team = Team.objects.all
    return render(request, 'pages/about.html' , { 'teams' : team })


def services(request):
    return render(request , 'pages/services.html')


def contact(request):
    return render(request , 'pages/contact.html')