from django import forms
from .models import Volontaire




class VolontaireForm(forms.ModelForm):

	class Meta:		
		model = Volontaire
		fields=['prenom_vol', 'nom_vol', 'groupe', 'tel_vol', 'mail_vol', ]

		labels = {
				"prenom_vol": "Prénom",
				"nom_vol": "Nom de famille",
				"tel_vol": "Numéro de téléphone",
				"mail_vol": " Adresse e-mail",
				"groupe": "Groupe",
			}

class Add_VolontaireForm(forms.ModelForm):
	intermediaire = forms.BooleanField(required=False)
	class Meta:		
		model = Volontaire
		fields=['prenom_vol', 'nom_vol', 'groupe', 'tel_vol', 'mail_vol', ]

		labels = {
				"prenom_vol": "Prénom",
				"nom_vol": "Nom de famille",
				"tel_vol": "Numéro de téléphone",
				"mail_vol": " Adresse e-mail",
				"groupe": "Groupe",
				"intermediaire": "Intermediaire",
			}

		help_texts={
				"intermediaire" : "Si vous souhaitez pouvoir servir d\'intermédiaire entre un volontaire et votre contact.",
					}	


class Ressource_VolontaireForm(forms.ModelForm):

	class Meta:		
		model = Volontaire
		fields=['prenom_vol', 'nom_vol', 'groupe', ]

		labels = {
				"prenom_vol": "Prénom",
				"nom_vol": "Nom de famille",
				"groupe": "Groupe",
			}