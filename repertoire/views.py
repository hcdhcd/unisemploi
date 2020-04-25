from django.shortcuts import render
from django.utils import timezone
from repertoire.models import Metier, Secteur, Contact
from utilisateurs.models import Volontaire
from repertoire.forms import RessourceForm, RequeteForm
from utilisateurs.forms import Ressource_VolontaireForm, VolontaireForm





def annuaire(request):

	metiers = Metier.objects.all()


	for metier in metiers:
		if not metier.contact_set.all():
			metiers=metiers.exclude(pk=metier.pk)


	return render(request, 'repertoire.html', {'metiers' : metiers})


def detailMetier(request, pk):
	metier=Metier.objects.get(pk=pk)
	contacts=metier.contact_set.all()
	x=len(contacts)

	return render(request, 'detailMetier.html', {'contacts' : contacts, 'metier':metier, 'x':x, }, )


def add_file(request, classe, pk):
	Classe=eval(classe)
	objet=Classe.objects.get(pk=pk)
	if request.method == 'POST' :

		form=RessourceForm(request.POST, request.FILES)
		form_vol = Ressource_VolontaireForm(request.POST or None)

		

		if form.is_valid() and form_vol.is_valid():
			validate=1

			ressource=form.save(commit=False)
			ressource.date_pub=timezone.now()

			"""je crée ou associe le vol a la ressource selon sil existe dans la db ou pas"""
			vol=Volontaire.objects.filter(prenom_vol__iexact=form_vol.cleaned_data['prenom_vol'], nom_vol__iexact=form_vol.cleaned_data['nom_vol'], groupe=form_vol.cleaned_data['groupe'])
			if vol:
				vol=vol.get(prenom_vol__iexact=form_vol.cleaned_data['prenom_vol'], nom_vol__iexact=form_vol.cleaned_data['nom_vol'], groupe=form_vol.cleaned_data['groupe'])
			else:
				vol=form_vol.save()

			ressource.vol=vol
			ressource.save()	
			"""je fais un lien avec l'objet a laquelle la ressource est associée"""
			if Classe == Metier:
				ressource.metier.set([objet,])

			if Classe == Secteur:	
				ressource.secteur.set([objet,])

			ressource.save()


		else:

			validate=0
	else:
		form=RessourceForm()

		form_vol=Ressource_VolontaireForm()

	return render(request, 'add_file.html', locals() )


def prendre_contact(request, classe, pk):
	Classe=eval(classe)
	objet=Classe.objects.get(pk=pk)

	if Classe == Metier or Classe == Secteur:
		type='un(e)'
	if Classe == Contact:
		type='ce'

	form_vol=VolontaireForm(request.POST or None)
	form=RequeteForm(request.POST or None)
	if form_vol.is_valid() and form.is_valid():

		requete = form.save(commit=False)
		requete.date_pub=timezone.now()

		"""j'associe la demande en fonction de son type"""
		if Classe == Contact:
			requete.contact.set([objet,])
		if Classe == Metier:
			requete.metier.set([objet,])
		if Classe == Secteur:
			requete.secteur.set([objet,])

		"""je crée ou associe le vol a la ressource selon sil existe dans la db ou pas"""
		vol=Volontaire.objects.filter(prenom_vol__iexact=form_vol.cleaned_data['prenom_vol'], nom_vol__iexact=form_vol.cleaned_data['nom_vol'], groupe=form_vol.cleaned_data['groupe'])
		if vol:
			vol=vol.get(prenom_vol__iexact=form_vol.cleaned_data['prenom_vol'], nom_vol__iexact=form_vol.cleaned_data['nom_vol'], groupe=form_vol.cleaned_data['groupe'])
		else:
			vol=form_vol.save()

		requete.vol=vol
		ressource.save()

	return render(request, 'prendre_contact.html', locals())

