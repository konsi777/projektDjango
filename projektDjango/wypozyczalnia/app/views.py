from django.shortcuts import render, redirect
from .models import Auto, Klient, Wypozyczenie
from .forms import WypozyczenieForm, KlientForm
from datetime import datetime
# Create your views here.

def base(request):
    return render(request, "index.html")

def rezerwacje(request):
    # Sprawdzenie czy data_zwrotu wypożyczenie jest taka sama jak dzisiejsza data,
    # nastepnie usuniecie tego rekordu wypożyczenia i zaaktualizaowanie dostępności wypożyczonego auta.
    wypozyczenia = Wypozyczenie.objects.filter(data_zwrotu=datetime.now())
    for wypozyczenie in wypozyczenia:
        if wypozyczenie:
            auto = Auto.objects.get(pk=wypozyczenie.auto.id)
            auto.dostepnosc=True
            auto.save()
            wypozyczenie.delete()

    

    if request.method == 'POST':
        auta = Auto.objects.all().order_by('-rocznik')
    else:
        auta = Auto.objects.all()
    
    context = {
          'auta': auta,
    }
    return render(request, 'rezerwacje.html', context)

def wypozyczenie(request, auto_id):
    pk = Auto.objects.get(pk=auto_id).id
    if request.POST:
        form_klient = KlientForm(request.POST)
        form_wypozyczenie = WypozyczenieForm(request.POST)
        if form_klient.is_valid() and form_wypozyczenie.is_valid():
            # Zapisanie nowego Klienta
            data_klient = form_klient.cleaned_data
            form_klient.save(data_klient)

            data_wypozyczenie = form_wypozyczenie.cleaned_data["data_wypozyczenia"]
            data_zwrotu = form_wypozyczenie.cleaned_data["data_zwrotu"]

            # Zapisanie nowego wypozyczenie z wybranym autem, datą i stworzonym przez uzytownika Klientem
            new_wypozyczenie = Wypozyczenie(klient=Klient.objects.last(), auto=Auto.objects.get(pk=pk), data_wypozyczenia=data_wypozyczenie , data_zwrotu=data_zwrotu)
            new_wypozyczenie.save()

            # Zmiana dostepności auta po wypozyczeniu przez klienta
            dostepnosc = Auto.objects.get(pk=pk)
            dostepnosc.dostepnosc=False
            dostepnosc.save()

            return redirect(rezerwacje)
    
    context = {
                'form_klient': KlientForm,
               'form_wypozyczenie': WypozyczenieForm,
               'auto': pk 
               }
    return render(request, "wypozyczenie.html", context)
