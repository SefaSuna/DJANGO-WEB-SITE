from datetime import date, datetime
from unicodedata import name
from django import http
from django.shortcuts import render,redirect,HttpResponse,get_object_or_404,reverse
from django.contrib.auth.models import User
from matplotlib.pyplot import title
from .models import comment
from .models import Data
from .forms import dataform

# Create your views here.
# 

def add_veri(request):
    form=dataform(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return render(request,"index.html")
    return render(request,"add.html",{"form":form})

def detail_veri(request,id):
    data=get_object_or_404(Data,id=id)
    comments=data.comments.all()

    return render(request,"data_detail.html",{"data":data,"comments":comments})

def commentt_veri(request,id):
    data=get_object_or_404(Data,id=id)
    if request.method == "POST":
        ad=request.POST.get("ad")
        yorum=request.POST.get("yorum")
        com=comment(ad=ad,yorum=yorum,date=datetime.now())
        com.article=data
        com.save()
        return redirect(reverse("detail_veri",kwargs={"id":id}))

#    return render(request,"detail.html",{"data":data,"com":comment})
def veri(request):
    data=Data.objects.all()
    return render(request,"veri.html",{"data":data})


def machine_desktop(request):
    data=get_object_or_404(Data,id=9)
    comments=data.comments.all()
    return render(request,"machine_desktop.html",{"data":data,"comments":comments})
    
