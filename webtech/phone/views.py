from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.
def home(request):
    product = Product.objects.all()
    
    return render(request,'home.html',{
        'Pro': product
    })


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def phone(request):
    return render(request,'phone.html')