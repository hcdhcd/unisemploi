from django import forms
from .models import Contact, Secteur, Ressource, Requete



class ContactForm(forms.ModelForm):

	
	class Meta:
		model = Contact
		fields = ['ajoute_par', 'vol_visible', 'prenom', 'nom', 'metier', 'dispo', 'tel', 'mail', 'ville', ]
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

class RessourceForm(forms.ModelForm):

	
	class Meta:
		model = Ressource
		fields=['titre', 'fichier']
		

class RequeteForm(forms.ModelForm):


	
	class Meta:
		model = Requete
		fields = ['dispo_vol', 'commentaire_vol', ]
		labels = {
			"dispo_vol": "Vos displonibilité(s) préférée(s)",
			"commentaire_vol":"Message",
		}

		help_texts = {
            "commentaire_vol": "Vous pouvez mettre ici tout ce qu'il vous semble à propos ... Préférences d'horaires, de lieu, message à destination du contact, des admins ... et bien d'autres",
            
        }

class RessourceForm(forms.ModelForm):

	
	class Meta:
		model = Ressource
		fields=['titre', 'fichier']



