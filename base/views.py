from django.shortcuts import render
from django.utils import timezone
from repertoire.models import Metier
from .models import AddContact
from .forms import AddContactForm, MessageForm
from utilisateurs.forms import VolontaireForm 


def apropos(request):

	return render(request, 'apropos.html')

def contact(request):

	form = MessageForm(request.POST or None)
	
	validate=0

	if request.method == "POST":
		if form.is_valid():
			form.save()

			validate= 1

		return render(request, 'contact.html', locals())





	return render(request, 'contact.html', locals())


def add_contact(request):



	form = AddContactForm(request.POST or None)
	
	if request.method == "POST":
		if form.is_valid():
			post = form.save(commit=False)
			post.date= timezone.now()
			post.save()

			validate=1

		return render(request, 'add_contact.html', locals())

	else:
		validate=0
		form = AddContactForm()


		
		

	return render(request, 'add_contact.html', locals())

def valid(request):
	contacts = AddContact.objects.all()



	return render(request, 'valid.html', locals())



