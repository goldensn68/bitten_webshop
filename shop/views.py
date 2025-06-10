from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Velkommen til Bitten webshop!</h1><p>Siden er online.</p>")
