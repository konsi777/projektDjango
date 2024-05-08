from django.shortcuts import render, redirect
from .models import Auto, Klient, Wypozyczenie
# Create your views here.

def base(request):
    return render(request, "index.html")

def rezerwacje(request):
    auta = Auto.objects.all()
    context = {
          'auta': auta
    }
    
    return render(request, 'rezerwacje.html', context)

def wypozyczenie(request):
    return render(request, "wypozyczenie.html")
