from django import forms
from .models import Contact, Secteur



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



