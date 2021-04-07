from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
from . models import product
def index(request):
    cats=product.objects.values("category")
    allProds=[]
    fcats={cat["category"] for cat in cats}
    for cat in fcats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides)])

    parms ={"all_prod":allProds}
    return render(request,'index.html',parms)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def products(request,myid):
    prod=product.objects.filter(id=myid)
    return render(request,'product.html',{'product':prod[0]})