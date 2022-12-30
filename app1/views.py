from django.shortcuts import render
from app1.models import Profession
def index_page(reqest):
    data ={
        'profession': Profession.objects.get(id=1)
    }
    return render(reqest, 'index.html', context=data)
def vacan_page(regest):
    return render(regest, 'vacan.html')

def habilities_page(reqest):
    return render(reqest,'habi.html')

def geo_page(reqest):
    return render(reqest,'geo.html')

def deman_page(reqest):
    return render(reqest,'demand.html')

# Create your views here.
