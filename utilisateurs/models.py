from django.db import models
from django.contrib.auth.models import User
from base.models import AdminCheck
from django.utils import timezone



class Volontaire(AdminCheck):

	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True) 

	"""	groupes=choices('Non Unis'
			'Connectes/emplois',
			'JCN Chèque énergie',
			'Colomiers',
			'Cinema et citoyenneté',
			
			)
	"""
	GROUPE_CHOICES = [
		
		('01', 'Connectés/Emploi'),
		('02', 'JCN/Chèque Energie'),
		('03', 'Colomiers'),
		('04', 'Cinéma et citoyenneté'),
		('na', 'N\'appartient pas à Unis-Cité'),
	]

	prenom_vol = models.CharField(max_length=30)
	nom_vol = models.CharField(max_length=30)
	groupe = models.CharField(max_length=2, choices=GROUPE_CHOICES, default='01' )
	
	tel_vol = models.CharField(max_length=10, blank=True, null=True)
	mail_vol = models.EmailField(blank=True, null=True)

	date_pub = models.DateTimeField(default=timezone.now)
	



	class Meta:
		verbose_name = "Volontaire"
	
	def __str__(self):

		return "{0} {1}".format(self.prenom_vol, self.nom_vol)

