from django.shortcuts import render,redirect
from .models import comment
from .forms import frm
def gbook(request):
    comments=comment.objects.order_by("-date")
    context={
        "data":comments,
    }
    return render(request,"guestbook/index.html",context)


def sign(request):
    if request.method=="POST":
        new_comment=comment(name=request.POST['name'],comment=request.POST['comment'])
        new_comment.save()
        return redirect("index")
    
    fm=frm()
    context={
        "form":fm
    }        
    return render(request,'guestbook/sign.html',context)
