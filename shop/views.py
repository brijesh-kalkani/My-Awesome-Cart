from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse('AboutAs')

def contact(request):
    return HttpResponse('contact us')

def tracker(request):
    return HttpResponse('TrackingStatus')

def search(request):
    return HttpResponse('search')

def productview(request):
    return HttpResponse('views')

def checkout(request):
    return HttpResponse('checkout')
