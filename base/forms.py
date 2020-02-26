from django import forms
from repertoire.models import Contact, Secteur
from.models import AddContact, Message



class MessageForm(forms.ModelForm):

	
	class Meta:

		exclude=['lu', 'traite', ]
		model = Message


class AddContactForm(forms.ModelForm):

	
	class Meta:
		model = AddContact
		exclude = ['date', ]

		labels = {
			"prenomV": "Prénom",
			"nomV": "Nom de famille",
			"telV": "Numéro de téléphone",
			"mailV": " Adresse e-mail",
			"groupeV": "Groupe",
			"vol_visible": "Intermediaire",
			"prenom": "Prénom",
			"nom": "Nom de famille",
			"tel": "Numéro de téléphone",
			"mail": " Adresse e-mail",
			"ville":"Ville(s)(facultatif)",
			"dispo": "Disponibilités",
			"metier0": "Métier",
			"secteur0": "Secteur",
			"metier1": "Métier",
			"secteur1": "Secteur",
			"metier2": "Métier",
			"secteur2": "Secteur",
			"metier3": "Métier",
			"secteur3": "Secteur",
			"metier4": "Métier",
			"secteur4": "Secteur",



			}
