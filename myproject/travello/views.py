from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.image = "destination_1.jpg"
    dest1.desc = "The city never sleeps"
    dest1.price = 700

    dest2 = Destination()
    dest2.name = "Hyderabad"
    dest2.image = "destination_2.jpg"
    dest2.desc = "The city of dreams"
    dest2.price = 800

    dest3 = Destination()
    dest3.name = "Banglore"
    dest3.image = "destination_3.jpg"
    dest3.desc = "The city of love"
    dest3.price = 900
    
    dests = [dest1,dest2,dest3]

    return render (request,"index.html",{'dests':dests})