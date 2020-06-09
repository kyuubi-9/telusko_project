from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.desc = 'The city that Never sleeps'
    dest1.img = "destination_1.jpg"
    dest1.price = 700
    dest1.offer = False

    dest2 = Destination()
    dest2.name = "Lucknow"
    dest2.desc = 'Best briyani'
    dest2.img = "destination_2.jpg"
    dest2.price = 600
    dest2.offer = True

    dest3 = Destination()
    dest3.name = "KOlkata"
    dest3.desc = 'hawda bridge'
    dest3.img = "destination_3.jpg"
    dest3.price = 800
    dests = [dest1,dest2,dest3]
    dest3.offer = False

    return render(request,'index.html',{'dests':dests})



    
