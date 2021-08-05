from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'swiggy/home.html')
def login(request):
    return render(request, 'swiggy/login.html')
def order(request):
    return render(request, 'swiggy/order.html')
