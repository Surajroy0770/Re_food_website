from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
from math import ceil


# Create your views here.
def index(request):
    # products=Product.objects.all()
    # print(products)
    # n=len(products)
    # nSlides=n//4 + ceil((n/4)-(n//4))
    # param={'no_of_slides':nslide,'range':range(1,nslide),'product':product}
    # allProds=[[products, range(1, nSlides), nSlides],
    #           [products, range(1, nSlides), nSlides]]


    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}

    for cat in cats:
        Prod=Product.objects.filter(category=cat)
        n=len(Prod)
        nSlides=n//4 + ceil((n/4)-(n//4))
        allProds.append([Prod,range(1,nSlides),nSlides])


    params={'allProds':allProds }
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        number=request.POST.get('number','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,number=number,desc=desc)
        contact.save()
    return render(request,'shop/contact.html')

def trackeer(request):
    return render(request,'shop/trackeer.html')

def search(request):
    return render(request,'shop/search.html')

def products(request,myid):
    product=Product.objects.filter(id=myid)
    return render(request,'shop/productView.html',{'product':product[0]})

def checkout(request):
    return render(request,'shop/checkout.html')