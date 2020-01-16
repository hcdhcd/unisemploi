from django.contrib import admin

from .models import Contact, Metier, Secteur

admin.site.register(Contact)
admin.site.register(Metier)
admin.site.register(Secteur)