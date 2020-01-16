from django.shortcuts import render
from repertoire.models import Metier
from .forms import ContactForm



def annuaire(request):

	metiers = Metier.objects.all()

	return render(request, 'repertoire.html', {'metiers' : metiers})

def apropos(request):

	return render(request, 'apropos.html')

def contact(request):

	return render(request, 'contact.html')

def add_contact(request):

	form = ContactForm(request.POST or None)

	if form.is_valid():
		prenom = form.cleaned_data['prenom']

	return render(request, 'add_contact.html', locals())

