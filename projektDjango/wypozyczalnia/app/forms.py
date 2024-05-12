from datetime import datetime
from django.forms import ModelForm
from django import forms
from .models import Klient

class WypozyczenieForm(ModelForm):
    imie = forms.CharField(max_length=50)
    nazwisko = forms.CharField(max_length=50)
    adres = forms.CharField(max_length=100)
    wiek = forms.IntegerField()
    telefon = forms.CharField(max_length=12)
    mail = forms.EmailField()
    # data_wypozyczenia = forms.DateField(default=datetime.now())
    # data_zwrotu = forms.DateField()
    class Meta:
        model = Klient
        fields = ['imie', 'nazwisko', 'adres', 'wiek', 'telefon', 'mail']