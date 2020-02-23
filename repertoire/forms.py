from django import forms
from .models import Contact, Secteur, AddContact




class ContactForm(forms.ModelForm):

	metier=forms.CharField(max_length=30, required=True)
	secteur=forms.CharField(max_length=30, required=True)
	
	class Meta:
		model = Contact
		fields = ['prenom', 'nom', 'tel', 'mail', 'ville', 'dispo',]
		labels = {
			"prenom": "Prénom",
			"nom": "Nom de famille",
			"tel": "Numéro de téléphone",
			"mail": " Adresse e-mail",
			"ville":"Ville(s)(facultatif)",
			"dispo": "Disponibilités",

		}

		help_texts = {
            "ville": "exemple : \"Toulouse, Lyon, ...\"",
            
        }


class AddContactForm(forms.ModelForm):

	metier=forms.CharField(max_length=30, required=True)
	secteur=forms.CharField(max_length=30, required=True)
	
	class Meta:
		model = AddContact
		fields = '__all__'

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

