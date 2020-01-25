from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import flights
# Create your views here.
def index(request):
    context={
        "flights":flights.objects.all()
    }
    return render(request,"flights/index.htm",context)

def flight(request,flight_id):
    try:
        f=flights.objects.get(pk=flight_id)
    except flights.DoesNotExist:
        raise Http404("flight deosnt exsist")
    context={
        "flight":f
    }
    return render(request,"flights/flight.htm",context)
    