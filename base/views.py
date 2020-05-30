from django.shortcuts import render, redirect
from django.utils import timezone
from repertoire.models import Metier, Secteur
from repertoire.forms import ContactForm
from .forms import Add_ContactForm, Add_ContactMetierForm, Add_ContactSecteurForm, MessageForm
from utilisateurs.forms import Add_VolontaireForm 
from utilisateurs.models import Volontaire
from base.fonctions import ListRepeatRemover


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

	form_vol = Add_VolontaireForm(request.POST or None)
	form_contact = Add_ContactForm(request.POST or None)
	form_metier = Add_ContactMetierForm(request.POST or None)
	form_secteur = Add_ContactSecteurForm(request.POST or None)

	if form_vol.is_valid() and form_contact.is_valid() and form_metier.is_valid() and form_secteur.is_valid():

		vol=Volontaire.objects.filter(prenom_vol__iexact=form_vol.cleaned_data['prenom_vol'], nom_vol__iexact=form_vol.cleaned_data['nom_vol'], groupe=form_vol.cleaned_data['groupe']) 

		if vol:
			vol=vol.get(prenom_vol__iexact=form_vol.cleaned_data['prenom_vol'], nom_vol__iexact=form_vol.cleaned_data['nom_vol'], groupe=form_vol.cleaned_data['groupe'])

			"""je crée le volontaire dans la db"""

		else:
			vol=form_vol.save()




		contact=form_contact.save()
	
		contact.ajoute_par=vol
		"""		contact.ajoute_par.add(vol)
		"""

		metiers=list(form_metier.cleaned_data.values())
		secteurs=list(form_secteur.cleaned_data.values())

		for i in range(5):
			m=metiers[i]
			s=secteurs[i]
			if metiers[i]:

				if Metier.objects.filter(metier__iexact=m):
					m=Metier.objects.get(metier__iexact=m)
					

				else : 

					m=Metier(metier=m)
					m.save()

				contact.metier.add(m)
				contact.save()

				if Secteur.objects.filter(secteur__iexact=s):
					s=Secteur.objects.get(secteur__iexact=s)
					

				else:
					s=Secteur(secteur=s)
					s.save()

				m.secteur.add(s)
				m.save()


		contact.save()
		
		validate=1
		required=form_vol.cleaned_data['intermediaire']

		return render(request, 'add_contact.html', locals())

	else:
		validate=0
		form_vol = Add_VolontaireForm(request.POST or None)
		form_contact = Add_ContactForm(request.POST or None)

		

	return render(request, 'add_contact.html', locals())

def add_contactjs(request):
	metiers = Metier.objects.all()
	secteurs=Secteur.objects.all()
	form_vol = Add_VolontaireForm(request.POST or None)
	form_contact = Add_ContactForm(request.POST or None)
	validate=0
	return render(request, 'add_contactjs.html', locals())





