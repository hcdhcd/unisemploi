from django import forms
from repertoire.models import Contact, Secteur
from.models import Message
from utilisateurs.models import Volontaire



class MessageForm(forms.ModelForm):	
	class Meta:

		model = Message
		fields=['titre', 'contenu', ]





class Add_ContactForm(forms.ModelForm):

	class Meta:

		model = Contact

		fields=[
				'prenom',
				'nom',
				'tel',
				'mail', 
				'ville',
				'dispo', 
				]

		labels = {
				"prenom" : "Prénom",
				"nom": "Nom de famille",
				"tel": "Numéro de téléphone",
				"mail": " Adresse e-mail",
				"ville":"Ville(s)(facultatif)",
				"dispo": "Disponibilités",
				}


class Add_ContactMetierForm(forms.Form):
	metier0=forms.CharField(max_length=30)
	metier1=forms.CharField(max_length=30, required=False)
	metier2=forms.CharField(max_length=30, required=False)
	metier3=forms.CharField(max_length=30, required=False)
	metier4=forms.CharField(max_length=30, required=False)

	class Meta:
		fields='__all__'
		labels = {
				"metier0": "Métier",
				"metier1": "Métier",
				"metier2": "Métier",
				"metier3": "Métier",
				"metier4": "Métier",
				}	

class Add_ContactSecteurForm(forms.Form):

	secteur0=forms.CharField(max_length=30)
	secteur1=forms.CharField(max_length=30, required=False)
	secteur2=forms.CharField(max_length=30, required=False)
	secteur3=forms.CharField(max_length=30, required=False)
	secteur4=forms.CharField(max_length=30, required=False)

	class Meta:
		fields='__all__'
		labels = {
				"secteur0": "Secteur",
				"secteur1": "Secteur",
				"secteur2": "Secteur",
				"secteur3": "Secteur",
				"secteur4": "Secteur",
				}