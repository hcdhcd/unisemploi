from django import forms
from .models import Contact, Secteur




class ContactForm(forms.ModelForm):
	ajout_metier = forms.CharField(max_length=30, label = "Nouveau Métier", required=False)
	ajout_secteur = forms.CharField(max_length=30, label = "Nouveau Secteur", required=False)
	secteur = forms.ModelMultipleChoiceField(queryset=Secteur.objects.all())
	
	class Meta:
		model = Contact
		fields = ['prenom', 'nom', 'tel', 'mail', 'ville', 'dispo', 'metier', 'ajout_metier', 'secteur', 'ajout_secteur']
		labels = {
			"prenom": "Prénom",
			"nom": "Nom de famille",
			"tel": "Numéro de téléphone",
			"mail": " Adresse e-mail",
			"ville":"Ville(s)(facultatif)",
			"dispo": "Disponibilités",
			"metier": "Métier",
		}

		help_texts = {
            "ville": "exemple : \"Toulouse, Lyon, ...\"",
            "metier":"maintenir la touche CTRL pour selectionner plusieurs métiers"
        }


