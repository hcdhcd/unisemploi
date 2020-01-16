from django.shortcuts import render
from repertoire.models import Metier



def annuaire(request):

	metiers = Metier.objects.all()

	return render(request, 'repertoire.html', {'metiers' : metiers})

def apropos(request):

	return render(request, 'apropos.html')

def contact(request):

	return render(request, 'contact.html')
