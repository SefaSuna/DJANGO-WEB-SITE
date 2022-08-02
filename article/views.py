from datetime import date, datetime
from unicodedata import name
from django import http
from django.shortcuts import render,redirect,HttpResponse,get_object_or_404,reverse
from django.contrib.auth.models import User
from matplotlib.pyplot import title
from .models import Article,comment
from .forms import aricleform
from data.models import Data
from django.db.models.functions import Upper

# Create your views here.
def index(request):
    ar=request.GET.get("search")
  
    if ar:
        article=Article.objects.filter(title__contains=ar)
        data=Data.objects.filter(title__contains=ar)
        return render(request,"index.html",{"article":article,"data":data})
    article=Article.objects.filter()
    data=Data.objects.filter()
    return render(request,"index.html",{"article":article,"data":data})
def about(request):
    return render(request,"about.html")
def add(request):
    form=aricleform(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return render(request,"index.html")
    return render(request,"add.html",{"form":form})

def detail(request,id):
    article=get_object_or_404(Article,id=id)
    comments=article.comments.all()

    return render(request,"detail.html",{"article":article,"comments":comments})

def commentt(request,id):
    article=get_object_or_404(Article,id=id)
    print("sefa")
    if request.method == "POST":
        ad=request.POST.get("ad")
        yorum=request.POST.get("yorum")
        com=comment(ad=ad,yorum=yorum,date=datetime.now())
        com.article=article
        com.save()
        print(ad)
        print(yorum)
        
        return redirect(reverse("detail",kwargs={"id":id}))

#    return render(request,"detail.html",{"article":article,"com":comment})
def yazılım(request):
    article=Article.objects.all()
    return render(request,"articles.html",{"article":article})


def desktop(request):
    article=get_object_or_404(Article,id=24)
    comments=article.comments.all()
    return render(request,"desktop.html",{"article":article,"comments":comments})