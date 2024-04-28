from django.db import models
# Create your models here.

class Klient(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    adres = models.CharField(max_length=100)
    wiek = models.PositiveIntegerField()
    telefon = models.CharField(max_length=20)
    mail = models.EmailField()

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'

class Auto(models.Model):
    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    typ = models.CharField(max_length=100)
    rocznik  = models.PositiveIntegerField()
    przebieg = models.PositiveIntegerField()
    moc_silnika = models.PositiveIntegerField()
    skrzynia = models.BooleanField()
    dostepnosc = models.BooleanField(default=True)
    cena_za_dobe = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.marka} {self.model}'

class Wypozyczenie(models.Model):
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    data_wypozyczenia = models.DateField()
    data_zwrotu = models.DateField()

    def __str__(self):
        return f'{self.klient} {self.auto.marka}'