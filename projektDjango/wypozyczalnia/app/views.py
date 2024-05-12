from django.shortcuts import render, redirect
from .models import Auto, Klient, Wypozyczenie
from .forms import WypozyczenieForm
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
    if request.POST:
        form = WypozyczenieForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(rezerwacje)
    return render(request, "wypozyczenie.html", {'form': WypozyczenieForm})
