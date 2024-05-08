from datetime import datetime
from django import forms
from .models import Wypozyczenie

class WypozyczenieForm(forms.ModelForm):
    imie = forms.CharField(max_length=50)
    nazwisko = forms.CharField(max_length=50)
    adres = forms.CharField(max_length=100)
    wiek = forms.IntegerField()
    telefon = forms.CharField(max_length=12)
    mail = forms.EmailField()
    data_wypozyczenia = forms.DateField(default=datetime.now())
    data_zwrotu = forms.DateField()
    class Meta:
        model = Wypozyczenie
        fields = ['imie', 'nazwisko', 'adres', 'wiek', 'telefon', 'mail', 'data_wypozyczenia', 'data_zwrotu']