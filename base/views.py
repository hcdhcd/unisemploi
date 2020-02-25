from django.shortcuts import render
from repertoire.models import Metier
from .models import AddContact
from .forms import AddContactForm
from utilisateurs.forms import VolontaireForm 


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
		
		form.save()	
		
		validate=1
		return render(request, 'add_contact.html', locals())

	return render(request, 'add_contact.html', locals())

def valid(request):
	contacts = AddContact.objects.all()



	return render(request, 'valid.html', locals())

