from django.shortcuts import render
from django.http import HttpResponse
from .models import product,offers

# Create your views here.


def index(request):
    pro=product.objects.all()
    context={"product":pro}
    return render(request,"index.htm",context)

def test1(request,num):
    return HttpResponse(f"it works {num}")


def forms(request):
    
    if request.method=="POST":
        print(request.POST['user'])
        return HttpResponse("done")

def get(request):
    return render(request,"user.htm")
    