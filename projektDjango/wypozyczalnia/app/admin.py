from django.contrib import admin
from .models import Auto, Wypozyczenie, Klient

# Register your models here.
admin.site.register(Auto)
admin.site.register(Wypozyczenie)
admin.site.register(Klient)