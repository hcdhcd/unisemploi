from django.db import models


class Volontaire(models.Model):

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

	prenom = models.CharField(max_length=30)
	nom = models.CharField(max_length=30)
	groupe = models.CharField(max_length=2, choices=GROUPE_CHOICES, default='01' )
	
	tel = models.CharField(max_length=10, blank=True, null=True)
	mail = models.EmailField(blank=True, null=True)



	class Meta:
		verbose_name = "Volontaire"
	
	def __str__(self):

		return "{0} {1}".format(self.prenom, self.nom)