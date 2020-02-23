from django.shortcuts import render
from repertoire.models import Metier
from .forms import ContactForm, AddContactForm
from utilisateurs.forms import VolontaireForm 



def annuaire(request):

	metiers = Metier.objects.all()


	for metier in metiers:
		if not metier.contact_set.all():
			metiers=metiers.exclude(pk=metier.pk)


	return render(request, 'repertoire.html', {'metiers' : metiers})

def apropos(request):

	return render(request, 'apropos.html')

def contact(request):

	return render(request, 'contact.html')

def add_contactpremier(request):

	validate = 0

	cform = AddContactForm(request.POST or None)
	vform = VolontaireForm(request.POST or None)

	if cform.is_valid() and vform.is_valid():

		cform = cform.cleaned_data
		vform = vform.cleaned_data
	
		
		validate=1
		return render(request, 'add_contact.html', locals())

	return render(request, 'add_contact.html', locals())

def add_contact(request):

	validate = 0

	form = AddContactForm(request.POST or None)
	
	if form.is_valid():
		form = form.cleaned_data	
		
		validate=1
		return render(request, 'add_contact.html', locals())

	return render(request, 'add_contact.html', locals())


