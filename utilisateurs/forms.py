from django import forms
from .models import Volontaire




class VolontaireForm(forms.ModelForm):

	vol_inter = forms.BooleanField(label='Intermediaire', help_text='Cochez cette case si vous souhaitez pouvoir servir d\'intermediaire entre d\'autres volontaires avec votre contact.', required=False )

	class Meta:
		model = Volontaire
		fields = ['prenom', 'nom', 'tel', 'mail', 'groupe', 'vol_inter']
		labels = {
			"prenom": "Prénom",
			"nom": "Nom de famille",
			"tel": "Numéro de téléphone",
			"mail": " Adresse e-mail",
			"groupe": "Groupe",
			}
