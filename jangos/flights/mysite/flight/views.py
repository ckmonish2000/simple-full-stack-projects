from django.shortcuts import render
from django.http import HttpResponse
from .models import flights
# Create your views here.
def index(request):
    context={
        "flights":flights.objects.all()
    }
    return render(request,"flights/index.htm",context)
    