import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wypozyczalnia.settings")
django.setup()

from app.models import Klient, Auto
cars_data = [
    {"marka": "Toyota", "model": "Corolla", "typ": "Sedan", "rocznik": 2018, "przebieg": 45000, "moc_silnika": 120, "skrzynia": 1, "dostepnosc": 1, "cena_za_dobe": 100},
    {"marka": "Ford", "model": "Focus", "typ": "Hatchback", "rocznik": 2017, "przebieg": 60000, "moc_silnika": 110, "skrzynia": 1, "dostepnosc": 1, "cena_za_dobe": 90},
    {"marka": "Volkswagen", "model": "Golf", "typ": "Hatchback", "rocznik": 2019, "przebieg": 30000, "moc_silnika": 150, "skrzynia": 1, "dostepnosc": 1, "cena_za_dobe": 120},
    {"marka": "BMW", "model": "3 Series", "typ": "Sedan", "rocznik": 2016, "przebieg": 70000, "moc_silnika": 180, "skrzynia": 1, "dostepnosc": 1, "cena_za_dobe": 150},
    {"marka": "Audi", "model": "A4", "typ": "Sedan", "rocznik": 2020, "przebieg": 20000, "moc_silnika": 200, "skrzynia": 1, "dostepnosc": 1, "cena_za_dobe": 180}
]

# Polish customer data
customers = [
    {"imie": "Jan", "nazwisko": "Kowalski", "adres": "ul. Półwiejska 12, Poznań", "wiek": 35, "telefon": "123-456-789", "mail": "jan@example.com"},
    {"imie": "Anna", "nazwisko": "Nowak", "adres": "ul. Gdańska 45, Gdynia", "wiek": 28, "telefon": "987-654-321", "mail": "anna@example.com"},
    {"imie": "Piotr", "nazwisko": "Wiśniewski", "adres": "ul. Krakowska 78, Kraków", "wiek": 40, "telefon": "555-555-555", "mail": "piotr@example.com"},
    {"imie": "Agnieszka", "nazwisko": "Wójcik", "adres": "ul. Warszawska 101, Warszawa", "wiek": 33, "telefon": "111-222-333", "mail": "agnieszka@example.com"},
    {"imie": "Marek", "nazwisko": "Lewandowski", "adres": "ul. Śląska 202, Katowice", "wiek": 45, "telefon": "999-888-777", "mail": "marek@example.com"}
]

# Create instances of Klient model with Polish data
for customer_data in customers:
    klient = Klient.objects.create(**customer_data)
    klient.save()


for car_data in cars_data:
    car = Auto.objects.create(**car_data)
    car.save()